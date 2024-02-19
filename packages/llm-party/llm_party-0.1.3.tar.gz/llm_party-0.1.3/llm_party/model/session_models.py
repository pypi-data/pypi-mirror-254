import yaml
from abc import ABC, abstractmethod, ABCMeta
from typing import Optional, List, Literal
from itertools import cycle
from llm_wrap.llm_response import get_response as get_ai_response
from llm_party.registry.attendee_registry import attendee_registry
from marshmallow import (
    Schema,
    fields,
    post_load,
    pre_load,
    ValidationError,
    validates_schema,
    EXCLUDE,
)

from marshmallow import (
    Schema,
    fields,
    post_load,
    ValidationError,
    validates_schema,
    EXCLUDE,
)
from datetime import datetime
from ..logger import get_logger
logging = get_logger()


class InstructionSchema(Schema):
    text = fields.Str(required=True)
    target = fields.Str(allow_none=True)
    version = fields.Str(allow_none=True)
    hash = fields.Str(allow_none=True)

    @post_load
    def make_instruction(self, data, **kwargs):
        return Instruction(**data)


class AttendeeSchema(Schema):
    type = fields.Str(required=True)
    name = fields.Str(required=True)
    role = fields.Str(required=True)
    instruction = fields.Nested(InstructionSchema, required=True)
    attendee_params = fields.Dict(required=True)  # allow_none=True)
    # Define the fields but exclude them by default
    llm_api = fields.Str(allow_none=True)
    llm_api_params = fields.Dict(allow_none=True)

    @pre_load
    def process_input(self, data, **kwargs):
        if attendee_registry.get(data["type"]):
            # No need to check for presence here, as they are optional and validated later
            pass
        else:
            # Remove LLMAgent-specific fields if present
            data.pop("llm_api", None)
            data.pop("llm_api_params", None)
        return data

    @post_load
    def make_attendee(self, data, **kwargs):
        attendee_type = data["type"]
        AttendeeClass = attendee_registry.get(attendee_type)
        if AttendeeClass is not None:
            return AttendeeClass(**data)
        else:
            raise ValidationError(f'The type must be a defined class and a subclass of Attendee. "{attendee_type}" does not meet these conditions.')


class MessageSchema(Schema):
    """
    Schema for serializing and deserializing Message objects.
    """

    sender = fields.Nested(AttendeeSchema, required=True)
    text = fields.Str(required=True)
    timestamp = fields.DateTime(format="%Y-%m-%dT%H:%M:%S", required=True)

    @post_load
    def make_message(self, data, **kwargs) -> "Message":
        """
        Create a Message object from deserialized data.

        Args:
            data (dict): Deserialized data.
            **kwargs: Additional keyword arguments.

        Returns:
            Message: A Message object.
        """
        return Message(**data)


class ChatSessionSchema(Schema):
    title = fields.Str(required=True)
    purpose = fields.Str(required=True)
    attendees = fields.List(fields.Nested(AttendeeSchema), required=True)
    settings = fields.Dict(keys=fields.Str(), values=fields.Raw(), required=True)
    start_at = fields.DateTime(format="%Y-%m-%dT%H:%M:%S", allow_none=True)
    updated_at = fields.DateTime(format="%Y-%m-%dT%H:%M:%S", allow_none=True)
    end_at = fields.DateTime(format="%Y-%m-%dT%H:%M:%S", allow_none=True)
    finish_reason = fields.Str(allow_none=True)
    status = fields.Str(required=True)
    chat_history = fields.List(fields.Nested(MessageSchema), allow_none=True)

    class Meta:
        unknown = EXCLUDE

    @post_load
    def make_chat_session(self, data, **kwargs):
        return ChatSession(**data)


class Instruction:
    def __init__(self, text, target=None, version=None, hash=None):
        self.update(text, target, version, hash)

    def update(self, text, target=None, version=None, hash=None):
        self.text = text
        self.target = target
        self.version = version
        self.hash = hash

class AttendeeMeta(ABCMeta):
    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        if name != 'Attendee':  # Avoid registering the base Attendee class
            attendee_registry.register(cls)


class Attendee(ABC, metaclass=AttendeeMeta):
    def __init__(self, name, role, instruction, attendee_params=None):
        if not isinstance(instruction, Instruction):
            raise TypeError("instruction must be an instance of Instruction")
        self.name = name
        self.role = role
        self.instruction = instruction
        self.attendee_params = attendee_params if attendee_params is not None else {}
        self.type = self.__class__.__name__

    def send_new_message(self, session: "ChatSession") -> "Message":
        response = self.generate_response(session.chat_history)
        message = Message(self, response)
        session.chat_history.append(message)
        return message

    @abstractmethod
    def generate_response(self, chat_history: List["Message"]) -> str:
        pass


class Human(Attendee):
    def __init__(self, name, role, instruction, attendee_params=None, **kwargs):
        super().__init__(name, role, instruction, attendee_params)
        # You can either store the extra kwargs or simply ignore them
        # For example, if you want to store them:
        self.extra_data = kwargs

    def generate_response(self, chat_history):
        raise NotImplementedError(
            "The generate_response method is not implemented for Human attendees."
        )


# TODO Make this an abstract class
class LLMAgent(Attendee):
    def __init__(
        self,
        name,
        role,
        instruction,
        attendee_params=None,
        llm_api=None,
        llm_api_params=None,
        **kwargs,
    ):
        super().__init__(name, role, instruction, attendee_params)
        self.llm_api = llm_api
        self.llm_api_params = llm_api_params if llm_api_params is not None else {}
        # Again, store or ignore the extra kwargs
        self.extra_data = kwargs


    # # TODO: @abstractmethod
    # def trait_instruction(self) -> str:
    #     # TODO: replace it with NotImplementedError
    #     return ""

    def generate_response(self, chat_history: List["Message"]) -> str:
        if self.llm_api is None:
            raise ValueError(
                "LLMAgent 'llm_api' attribute is not set to a supported API identifier. Please see the documentation for supported APIs in `llm_wrap` library."
            )

        messages = self.convert_chat_history_to_openai_messages(chat_history)

        logging.debug(f"messages (no system): {messages[1:]}")
        try:
            response = get_ai_response(
                llm_api=self.llm_api, messages=messages, **self.llm_api_params
            )
        except ValueError as e:
            raise ValueError(f"Error generating response: {str(e)}")

        return response

    @property
    def initial_instruction(self):
        if hasattr(self, "trait_instruction"):
            return self.instruction.text + "\n" + self.trait_instruction()
        else:
            return self.instruction.text

    def convert_chat_history_to_openai_messages(self, chat_history: List["Message"]) -> List[dict]:
        # Create the initial system message
        messages = [{"role": "system", "content": self.initial_instruction}]

        # Define the roles for the chat history messages
        roles = cycle(["user", "assistant"])

        # Convert each message in the chat history to the required format
        for message in chat_history:
            formatted_message = {"role": next(roles), "content": message.text}
            messages.append(formatted_message)

        return messages


class Message:
    def __init__(self, sender: Attendee, text: str, timestamp: Optional[datetime]=None):
        self.sender = sender
        self.text = text
        self.timestamp = timestamp if timestamp else datetime.now()

    @staticmethod
    def create(
        sender_name: str,
        sender_role: str,
        sender_type: str,
        sender_attendee_params: dict,
        text: str,
        instruction_text: str = "",
        instruction_target: str = None,
        instruction_version: str = None,
        instruction_hash: str = None,
    ) -> "Message":
        """
        Create a Message object.

        Args:
            sender_name (str): The name of the sender.
            sender_role (str): The role of the sender.
            sender_type (str): The type of the sender.
            sender_attendee_params (dict): The attendee parameters of the sender.
            text (str): The text of the message.
            instruction_text (str): The text of the instruction.
            instruction_target (str): The target of the instruction.
            instruction_version (str): The version of the instruction.
            instruction_hash (str): The hash of the instruction.

        Returns:
            Message: A Message object.
        """
        if instruction_target is None:
            instruction_target = ""
        if instruction_version is None:
            instruction_version = ""
        if instruction_hash is None:
            instruction_hash = ""
        instruction = Instruction(
            text=instruction_text,
            target=instruction_target,
            version=instruction_version,
            hash=instruction_hash,
        )

        if sender_type == "Human":
            sender = Human(
                name=sender_name,
                role=sender_role,
                type=sender_type,
                instruction=instruction,
                attendee_params=sender_attendee_params,
            )
        elif sender_type == "LLMAgent":
            sender = LLMAgent(
                name=sender_name,
                role=sender_role,
                type=sender_type,
                instruction=instruction,
                attendee_params=sender_attendee_params,
            )
        else:
            raise ValueError(
                f"Invalid sender_type: {sender_type}. Expected 'Human' or 'LLMAgent'."
            )

        return Message(sender=sender, text=text, timestamp=datetime.now())

    def to_openai_message(self):
        return {"role": self.sender.role, "content": self.text}

    def to_dict(self):
        schema = MessageSchema()
        return schema.dump(self)

class ChatSession:
    def __init__(
        self,
        title: str=None,
        purpose: str=None,
        attendees: List[Attendee]=None,
        settings: dict=None,
        start_at: datetime=None,
        updated_at: datetime=None,
        end_at: datetime=None,
        finish_reason: str=None,
        chat_history: List[Message]=None,
        status: Literal["initialized", "started", "paused", "resumed", "completed_successfully", "completed_with_failure", "cancelled"]="initialized",
    ):
        self.title = title
        self.purpose = purpose
        self.attendees = attendees if attendees is not None else []
        self.settings = settings if settings is not None else {}
        self.chat_history = chat_history if chat_history is not None else []
        self.finish_reason = finish_reason
        self.start_at = start_at
        self.updated_at = updated_at
        self.end_at = end_at
        self.status = status

    def add_attendee(self, attendee):
        if attendee not in self.attendees:
            self.attendees.append(attendee)
            self.updated_at = datetime.now()
        else:
            raise ValueError(f"Attendee {attendee.name} is already part of the session")

    def remove_attendee(self, attendee):
        try:
            self.attendees.remove(attendee)
            self.updated_at = datetime.now()
        except ValueError:
            raise ValueError(f"Attendee {attendee.name} is not part of the session")

    def configure(self, settings):
        self.settings = settings

    def start(self):
        self.start_at = datetime.now()
        self.updated_at = self.start_at
        self.status = "started"

    def end(self, status, finish_reason):
        self.status = status
        self.finish_reason = finish_reason
        self.end_at = datetime.now()

    def set_purpose(self, purpose):
        self.purpose = purpose

    def get_purpose(self):
        return self.purpose

    @staticmethod
    def from_json(json_string):
        schema = ChatSessionSchema()
        try:
            # Deserialize the JSON string into a dictionary
            data = schema.loads(json_string)
            # Check if data is already a ChatSession instance
            if isinstance(data, ChatSession):
                return data
            # Otherwise, create a new ChatSession instance using the deserialized data
            return ChatSession(**data)
        except ValidationError as err:
            raise ValueError(f"Invalid JSON data: {err.messages}")

    def to_json(self, pretty_print=False):
        """
        Serializes the ChatSession object to JSON.

        Returns:
            str: The serialized JSON representation of the ChatSession object.

        Raises:
            ValueError: If there is an error serializing the ChatSession object.
        """
        schema = ChatSessionSchema()
        try:
            if pretty_print:
                return schema.dumps(self, indent=4)
            else:
                return schema.dumps(self)
        except ValidationError as err:
            raise ValueError(f"Error serializing ChatSession: {err.messages}")

    def to_dict(self):
        """
        Converts the ChatSession object to a dictionary.

        Returns:
            dict: The dictionary representation of the ChatSession object.

        Raises:
            ValueError: If there is an error converting the ChatSession object.
        """
        schema = ChatSessionSchema()
        try:
            json_data = schema.dumps(self)
            return yaml.safe_load(json_data)
        except ValidationError as err:
            raise ValueError(f"Error converting ChatSession to dict: {err.messages}")

    def to_yaml(self):
        """
        Serializes the ChatSession object to YAML.

        Returns:
            str: The serialized YAML representation of the ChatSession object.

        Raises:
            ValueError: If there is an error serializing the ChatSession object.
        """
        try:
            dict_data = self.to_dict()
            return yaml.dump(dict_data, default_flow_style=False)
        except ValidationError as err:
            raise ValueError(f"Error serializing ChatSession to YAML: {err.messages}")

    def get_message_from_history(self, n: int) -> dict:
        """
        Returns the dictionary representation of the n-th message in the chat history.

        Args:
            n (int): The index of the message in the chat history. You can specify a negative index to get the message from the end of the chat history.

        Returns:
            dict: The dictionary representation of the n-th message in the chat history. The keys of the dictionary corresponds to the fields defined in MessageSchema.
        """
        if n < len(self.chat_history):
            return self.chat_history[n].to_dict()
        else:
            raise IndexError("Message index out of range.")

    def set_max_messages(self, value: int) -> None:
        """
        Set the max number of messages in the session settings.

        Args:
            value (int): The value to set for the max number of messages.
        """
        self.settings["max_sent_message"] = value

    def increase_max_messages(self, increment: int) -> None:
        """
        Increase the max number of messages by a specified increment. This property is used to control the number of turns in the session between agents.

        Args:
            increment (int): The amount to increase the max number of messages by.
        """
        if "max_sent_message" in self.settings:
            self.settings["max_sent_message"] += increment
        else:
            raise KeyError("The 'max_sent_message' setting does not exist.")

    @validates_schema
    def validate_chat_session(self, data, **kwargs):
        # Custom validation logic here
        pass

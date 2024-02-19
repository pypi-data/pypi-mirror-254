import hashlib
import time
import json
import os
from datetime import datetime
import tempfile
from typing import Any, Dict, Tuple, Literal, Callable, Optional
from ..logger import get_logger

logging = get_logger()
from ..model.session_models import ChatSession, Message, MessageSchema, Attendee
from llm_party.model import session_models


def start_session_with_user_first_message(
    config_file_path: str,
    first_message: str,
    sender_name: str = "Inquiry Sender",
    sender_role: str = "user",
    sender_type: Literal["Human", "Agent"] = "Human",
    sender_attendee_params: dict = {},
    save_dir: str = None,
    save_file_name: str = None,
    pretty_print=False,
    save_yaml=False,
    output: Optional[Callable[[str], None]] = None
) -> Tuple[ChatSession, str]:
    """
    This method initiates a chat session with a user's first message. It takes in the configuration file path,
    the first message from the user, and optional parameters about the sender and saving the chat session.
    It then creates a chat session, saves it, and returns the chat session object and the saved file path.

     Args:
        config_file_path (str): Path to the configuration file. This file should contain the initial settings for the chat session.
        first_message (str): The first message from the user to start the chat session.
        sender_name (str, optional): The name of the sender. Defaults to "Inquiry Sender".
        sender_role (str, optional): The role of the sender. Defaults to "user".
        sender_type (str, optional): The type of the sender. Defaults to "Human".
        sender_attendee_params (dict, optional): The attendee parameters of the sender. Defaults to {}.
        save_dir (str, optional): Directory to save the chat session object. Defaults to None.
        save_file_name (str, optional): Name of the file to save the chat session object. Defaults to None.

    Returns:
        Tuple[ChatSession, str]: Tuple of ChatSession object and the saved file path.

    Raises:
        ValueError: If there is an error reading the configuration file, creating or writing to the temporary file,
        or creating or serializing the first message, a ValueError is raised with a message indicating the source of the error.

    This method handles errors by catching exceptions during the reading of the configuration file,
    the creation of the temporary file, and the creation and serialization of the first message.
    If an error occurs during any of these steps, the method raises a ValueError with a message indicating the source of the error.
    """
    try:
        # Load the initial configuration from the configuration file
        with open(config_file_path, "r") as f:
            config = json.load(f)
    except Exception as e:
        raise ValueError(
            f"Error reading the configuration file {config_file_path}: {str(e)}"
        )

    # Add the serialized Message object to the configuration
    config["chat_history"].append(
        create_first_message(
            sender_name, sender_role, sender_type, sender_attendee_params, first_message
        )
    )
    try:
        # Save the updated configuration to a temporary file
        with tempfile.NamedTemporaryFile(mode="w+", delete=False) as temp_config_file:
            json.dump(config, temp_config_file)
            temp_config_file.flush()
            temp_config_file_path = temp_config_file.name
    except Exception as e:
        raise ValueError(f"Error creating or writing to the temporary file: {str(e)}")

    # Start the chat session with the updated configuration
    try:
        chat_session, saved_file_path = start_session(
            temp_config_file_path, save_dir=save_dir, save_file_name=save_file_name, pretty_print=pretty_print, save_yaml=save_yaml, output=output
        )
    finally:
        # Delete the temporary file
        os.remove(temp_config_file_path)

    return chat_session, saved_file_path


def create_first_message(
    sender_name: str,
    sender_role: str,
    sender_type: Tuple[Literal["Human"]], # LLMAgent will be added later
    sender_attendee_params: dict,
    first_message: str,
) -> Dict[str, Any]:
    """
    Create a serialized Message object for the user's first message.

    Args:
        sender_name (str): The name of the sender.
        sender_role (str): The role of the sender.
        sender_type (str): The type of the sender.
        sender_attendee_params (dict): The attendee parameters of the sender.
        first_message (str): The first message from the user.

    Returns:
        Dict[str, Any]: The serialized Message object.
    """
    if sender_type not in ["Human"]:
        raise ValueError("sender_type must be Human for the first message")
    try:
        # Create a Message object for the user's first message
        first_message_obj = Message.create(
            sender_name, sender_role, sender_type, sender_attendee_params, first_message
        )

        # Serialize the Message object
        message_schema = MessageSchema()
        first_message_serialized = message_schema.dump(first_message_obj)
    except Exception as e:
        raise ValueError(f"Error creating or serializing the first message: {str(e)}")

    return first_message_serialized


def start_session(
    config_file_path: str, save_dir: str = None, save_file_name: str = None, pretty_print=False, save_yaml=False, output: Optional[Callable[[str], None]] = None
) -> Tuple[ChatSession, str]:
    """
    Start a chat session based on the configuration file.

    Args:
        config_file_path: Path to the configuration file.
        save_dir: Directory to save the chat session object.
        save_file_name: Name of the file to save the chat session object.
        pretty_print: Whether to pretty print the chat session object. It only applies when save_yaml is False.
        save_yaml: Whether to save the chat session object as a YAML file. If False, it will be saved as a JSON file.

    Returns:
        Tuple of ChatSession object and the saved file path.
    """
    # Validate the configuration file
    validate_config_file(config_file_path)

    # Initialize the chat session
    chat_session = initialize_chat_session(config_file_path)

    # Progress the chat session
    chat_session, saved_file_path = progress_chat_session(
        chat_session, save_dir=save_dir, save_file_name=save_file_name, pretty_print=pretty_print, save_yaml=save_yaml, output=output
    )

    return chat_session, saved_file_path


def validate_config_file(config_file_path):
    # Check if the file exists and is accessible
    if not os.path.isfile(config_file_path):
        raise ValueError(
            f"The configuration file {config_file_path} does not exist or is not accessible"
        )

    try:
        with open(config_file_path, "r") as f:
            config = json.load(f)
    except Exception as e:
        raise ValueError(
            f"Error reading the configuration file {config_file_path}: {str(e)}"
        )

    # Check if there are more than two LLM agents
    llm_agents = [
        a
        for a in config["attendees"]
    ]
    if len(llm_agents) < 2:
        raise ValueError(
            "The configuration file must contain more than two agents"
        )

    # Check if llm_api_params includes valid OpenAI API parameters
    # TODO: This will be updated when llm_party supports other LLM APIs
    for agent in llm_agents:
        if "llm_api_params" not in agent:
            raise ValueError(f"Each LLM agent must have 'llm_api_params' field")

        params = agent["llm_api_params"]
        required_params = [
            "temperature",
            "top_p",
            "frequency_penalty",
            "presence_penalty",
        ]
        missing_params = [param for param in required_params if param not in params]
        if missing_params:
            raise ValueError(
                f"'llm_api_params' is missing the following OpenAI API parameters: {', '.join(missing_params)}"
            )

    # Check if max_sent_message is an integer and greater than 0
    max_sent_message = config["settings"]["max_sent_message"]
    if not isinstance(max_sent_message, int):
        raise ValueError("'max_sent_message' must be an integer")
    if max_sent_message <= 0:
        raise ValueError("'max_sent_message' must be greater than 0")


def initialize_chat_session(config_file_path):
    # Validate the configuration file
    validate_config_file(config_file_path)

    # Read the configuration file
    with open(config_file_path, "r") as f:
        config = f.read()

    # Initialize a ChatSession object
    try:
        chat_session = ChatSession.from_json(config)
    except ValueError as e:
        raise ValueError(f"Error initializing ChatSession: {str(e)}")

    return chat_session


def start_chat_session(chat_session):
    chat_session.start()


def send_messages(chat_session: ChatSession, output: Optional[Callable[[str], None]] = None):
    """
    "max_sent_message": 人間も含めたすべての参加者のメッセージ数の上限です
    """
    try:
        for _ in range(chat_session.settings["max_sent_message"]):
            for attendee in chat_session.attendees:
                try:
                    attendee.send_new_message(chat_session)
                    if output is not None:
                        # Print the latest message in the chat history
                        latest_message = chat_session.get_message_from_history(-1)
                        output("-----------------------------------------")
                        output(f"{latest_message['sender']['name']} ({latest_message['sender']['role']}):")
                        output(chat_session.get_message_from_history(-1)["text"])
                except ValueError as e:
                    raise ValueError(f"Error sending message: {str(e)}")
                if (
                    len(chat_session.chat_history)
                    >= chat_session.settings["max_sent_message"]
                ):
                    raise StopIteration  # Breaks both loops
    except StopIteration:
        chat_session.end("completed_successfully", "MaxSentMessage")
    except Exception as e:
        chat_session.end("completed_with_failure", f"LLMAPIFailure: {str(e)}")
        raise


def end_chat_session(chat_session):
    if chat_session.status == "started":
        chat_session.end("completed_successfully", "MaxSentMessage")


def serialize_chat_session(chat_session, save_dir=None, save_file_name=None, pretty_print=False, save_yaml=False):
    # Serialize the ChatSession object to a JSON file
    if save_file_name is None:
        save_file_name = (
            f"{chat_session.title}_{datetime.now().strftime('%Y%m%d%H%M%S')}.json"
        )
    if save_dir is not None:
        os.makedirs(save_dir, exist_ok=True)
        save_file_path = os.path.join(save_dir, save_file_name)
    else:
        save_file_path = save_file_name
    try:
        if save_yaml:
            dump_str = chat_session.to_yaml()
        else:
            dump_str = chat_session.to_json(pretty_print=pretty_print)
        with open(save_file_path, "w") as f:
            f.write(dump_str)
    except Exception as e:
        logging.error(f"Error serializing ChatSession: {str(e)}")
        chat_session.end("completed_with_failure", f"SerializationError: {str(e)}")
        raise

    return chat_session, save_file_path


def progress_chat_session(chat_session, save_dir=None, save_file_name=None, pretty_print=False, save_yaml=False, output: Optional[Callable[[str], None]] = None):
    start_chat_session(chat_session)
    send_messages(chat_session, output)
    logging.debug(
        f"[progress_chat_session] chat_session.chat_history: {chat_session.chat_history}"
    )
    end_chat_session(chat_session)
    return serialize_chat_session(chat_session, save_dir, save_file_name, pretty_print=pretty_print, save_yaml=save_yaml)

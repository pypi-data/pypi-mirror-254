import unittest
from unittest import skipIf
import json
import yaml
from unittest.mock import patch
from marshmallow import ValidationError
from llm_party.model.session_models import LLMAgent, Message
from llm_party.model.session_models import (
    Instruction,
    Attendee,
    Human,
    LLMAgent,
    Message,
    ChatSession,
    AttendeeSchema,
    MessageSchema,
    ChatSessionSchema
)


USE_ACTUAL_LLM_API = False


def skip_if_no_api():
    return skipIf(
        not USE_ACTUAL_LLM_API, "Skipping this test because USE_ACTUAL_LLM_API is False"
    )


# The return of this method is used a sample JSON to initialize ChatSession objects
def _get_init_json_data():
    return {
        "title": "Chat Session Title",
        "purpose": "Chat Session Purpose",
        "status": "initialized",
        "attendees": [
            {
                "type": "Human",
                "name": "John Doe",
                "role": "user",
                "instruction": {"text": "Say hello"},
                "attendee_params": {},
            },
            {
                "type": "LLMAgent",
                "name": "AI",
                "role": "assistant",
                "instruction": {"text": "Respond politely"},
                "attendee_params": {},
                "llm_api": "openai",
                "llm_api_params": {},
            },
        ],
        "settings": {},
        "chat_history": [],
        "finish_reason": None,
        "start_at": None,
        "updated_at": None,
        "end_at": None,
    }


class TestChatModels(unittest.TestCase):
    def setUp(self):
        # Create a JSON string with the necessary information
        session_init_json = _get_init_json_data()
        self.session = ChatSession(**session_init_json)
        instruction_for_human = Instruction("Say hello")
        instruction_for_agent = Instruction("Respond politely")
        self.instruction = Instruction("Test instruction")
        self.human = Human("John Doe", "user", instruction_for_human)
        self.agent = LLMAgent(
            "AI", "assistant", instruction_for_agent, llm_api="openai"
        )

    def test_instruction(self):
        # Initialize Instruction with some values
        self.instruction = Instruction(
            "Test instruction", "target_value", "version_value", "hash_value"
        )
        self.assertEqual(self.instruction.text, "Test instruction")
        self.assertEqual(self.instruction.target, "target_value")
        self.assertEqual(self.instruction.version, "version_value")
        self.assertEqual(self.instruction.hash, "hash_value")

        # Update the Instruction with new values
        self.instruction.update(
            "Updated instruction", "new_target", "new_version", "new_hash"
        )
        self.assertEqual(self.instruction.text, "Updated instruction")
        self.assertEqual(self.instruction.target, "new_target")
        self.assertEqual(self.instruction.version, "new_version")
        self.assertEqual(self.instruction.hash, "new_hash")

        # Update the Instruction with None values
        self.instruction.update("Another update", None, None, None)
        self.assertEqual(self.instruction.text, "Another update")
        self.assertIsNone(self.instruction.target)
        self.assertIsNone(self.instruction.version)
        self.assertIsNone(self.instruction.hash)

    def test_instruction_with_none_values(self):
        # Create Instruction with None values for target, version, and hash
        instruction = Instruction("Test instruction", None, None, None)
        self.assertEqual(instruction.text, "Test instruction")
        self.assertIsNone(instruction.target, "Target should be None")
        self.assertIsNone(instruction.version, "Version should be None")
        self.assertIsNone(instruction.hash, "Hash should be None")

    def test_attendee(self):
        self.assertEqual(self.human.name, "John Doe")
        self.assertEqual(self.human.role, "user")
        self.assertEqual(self.human.instruction.text, "Say hello")

    def test_chat_session(self):
        self.assertEqual(self.session.title, "Chat Session Title")
        self.assertEqual(self.session.purpose, "Chat Session Purpose")
        self.assertEqual(self.session.status, "initialized")  # Test the initial status
        self.session.start()
        self.assertEqual(
            self.session.status, "started"
        )  # Test the status after starting the session
        self.session.add_attendee(self.human)
        self.assertIn(self.human, self.session.attendees)
        self.session.remove_attendee(self.human)
        self.assertNotIn(self.human, self.session.attendees)

    def test_message(self):
        message = Message(self.human, "Hello, world!")
        self.assertEqual(message.sender, self.human)
        self.assertEqual(message.text, "Hello, world!")

    def test_llm_agent(self):
        self.assertEqual(self.agent.name, "AI")
        self.assertEqual(self.agent.role, "assistant")
        self.assertEqual(self.agent.instruction.text, "Respond politely")

    @skip_if_no_api()
    def test_llm_agent_generate_response(self):
        message = Message(self.human, "Hello, world!")
        response = self.agent.generate_response([message.to_openai_message()])
        self.assertIsNotNone(response)  # Ensure response is not None

    def test_chat_session_to_from_json(self):
        self.session.add_attendee(self.human)
        json_string = self.session.to_json()
        new_session = ChatSession("New Session", "Testing from_json")
        new_session.from_json(json_string)
        self.assertEqual(new_session.title, self.session.title)
        self.assertEqual(new_session.purpose, self.session.purpose)

    def test_chat_session_to_from_json(self):
        self.session.add_attendee(self.human)
        json_string = self.session.to_json()
        new_session = ChatSession.from_json(json_string)
        self.assertEqual(new_session.title, self.session.title)
        self.assertEqual(new_session.purpose, self.session.purpose)

    def test_attendee_send_new_message(self):
        # TODO: Test after implementing send_new_message
        # Human does not support send_new_message yet.
        # message = self.human.send_new_message(self.session)
        pass

    def test_edge_cases(self):
        # Test removing an attendee who is not in the session
        with self.assertRaises(ValueError):
            self.session.remove_attendee(self.agent)

        # Test from_json with invalid JSON string
        with self.assertRaises(ValueError):
            self.session.from_json("invalid json string")

    def test_chat_session_from_json_valid(self):
        valid_json = json.dumps(_get_init_json_data())
        # Use the from_json static method to create a ChatSession instance from the JSON string
        session = ChatSession.from_json(valid_json)
        self.assertEqual(session.title, "Chat Session Title")
        self.assertEqual(session.purpose, "Chat Session Purpose")
        self.assertEqual(len(session.attendees), 2)
        self.assertIsInstance(session.attendees[0], Human)
        self.assertIsInstance(session.attendees[1], LLMAgent)

    def test_remove_attendee_not_in_session(self):
        # Test removing an attendee who is not in the session
        with self.assertRaises(ValueError) as context:
            self.session.remove_attendee(self.agent)
        self.assertIn("Attendee AI is not part of the session", str(context.exception))

    def test_remove_attendee_from_empty_session(self):
        # Test removing an attendee from an empty session
        self.session.attendees = []  # Clear attendees
        with self.assertRaises(ValueError) as context:
            self.session.remove_attendee(self.human)
        self.assertIn(
            "Attendee John Doe is not part of the session", str(context.exception)
        )

    def test_remove_attendee_multiple_times(self):
        # Test removing the same attendee multiple times
        self.session.add_attendee(self.human)
        self.session.remove_attendee(self.human)
        with self.assertRaises(ValueError) as context:
            self.session.remove_attendee(self.human)
        self.assertIn(
            "Attendee John Doe is not part of the session", str(context.exception)
        )

    def test_remove_attendee_not_in_session(self):
        # Test removing an attendee who is not in the session
        with self.assertRaises(ValueError) as context:
            self.session.remove_attendee(self.agent)
        self.assertIn("Attendee AI is not part of the session", str(context.exception))


class TestLLMAgent(unittest.TestCase):
    @patch("llm_party.model.session_models.get_ai_response")
    def test_llm_agent_generate_response(self, mock_get_ai_response):
        # Setup the mock to return a predefined response
        mock_get_ai_response.return_value = "Mocked response"

        instruction_for_agent = Instruction("Respond politely")
        agent = LLMAgent("AI", "assistant", instruction_for_agent, llm_api="openai")
        message = Message(agent, "Hello, world!")
        response = agent.generate_response([message])

        # Assert that the mock was called as expected
        mock_get_ai_response.assert_called_once_with(
            llm_api="openai",
            messages=[
                {"role": "system", "content": agent.instruction.text},
                {"role": "user", "content": message.text},
            ],
            **agent.llm_api_params,
        )
        # Assert that the response is as expected
        self.assertEqual(response, "Mocked response")


class TestChatSessionSerialization(unittest.TestCase):
    def test_chat_session_serialization(self):
        # Given JSON data
        json_data = json.dumps(_get_init_json_data())
        # When deserializing the JSON string to a ChatSession object
        session = ChatSession.from_json(json_data)

        # Then the ChatSession object should have the same data as the JSON
        self.assertEqual(session.title, "Chat Session Title")
        self.assertEqual(session.purpose, "Chat Session Purpose")
        self.assertEqual(len(session.attendees), 2)
        self.assertIsInstance(session.attendees[0], Human)
        self.assertIsInstance(session.attendees[1], LLMAgent)
        self.assertEqual(session.attendees[0].name, "John Doe")
        self.assertEqual(session.attendees[1].name, "AI")
        self.assertEqual(session.attendees[0].instruction.text, "Say hello")
        self.assertEqual(session.attendees[1].instruction.text, "Respond politely")
        self.assertIsNone(session.finish_reason)
        self.assertIsNone(session.start_at)
        self.assertIsNone(session.updated_at)
        self.assertIsNone(session.end_at)


class TestAttendeeSchemaValidation(unittest.TestCase):
    def test_invalid_attendee_type(self):
        invalid_data = {
            "type": "UnknownType",
            "name": "Invalid Attendee",
            "role": "invalid",
            "instruction": {"text": "Invalid instruction"},
        }
        with self.assertRaises(ValidationError):
            AttendeeSchema().load(invalid_data)


class TestChatSessionTimes(unittest.TestCase):
    def test_start_session(self):
        session = ChatSession(title="Test Session", purpose="Testing")
        session.start()
        self.assertIsNotNone(session.start_at)
        self.assertEqual(session.start_at, session.updated_at)


class TestLLMAgentResponseGeneration(unittest.TestCase):
    @patch("llm_party.model.session_models.get_ai_response")
    def test_generate_response(self, mock_get_ai_response):
        mock_get_ai_response.return_value = "Mocked response"
        agent = LLMAgent(
            "AI", "assistant", Instruction("Respond politely"), llm_api="openai"
        )
        message = Message(agent, "Hello, world!")
        response = agent.generate_response([message])
        self.assertEqual(response, "Mocked response")


class TestAttendeeMessageSending(unittest.TestCase):
    def test_send_new_message(self):
        # TODO: Test after implementing send_new_message
        session = ChatSession(title="Test Session", purpose="Testing")
        human = Human("John Doe", "user", Instruction("Say hello"))
        session.add_attendee(human)
        # Human does not support send_new_message yet.
        # human.send_new_message(session)


class TestChatSessionErrorHandling(unittest.TestCase):
    def test_from_json_invalid_json(self):
        with self.assertRaises(ValueError):
            ChatSession.from_json("invalid json string")

    def test_add_existing_attendee(self):
        session = ChatSession(title="Test Session", purpose="Testing")
        human = Human("John Doe", "user", Instruction("Say hello"))
        session.add_attendee(human)
        with self.assertRaises(ValueError):
            session.add_attendee(human)


class TestAttendeeMethods(unittest.TestCase):
    def test_send_new_message(self):
        # Create a Human instance
        human = Human("John", "user", Instruction("Hello"))
        # Create a ChatSession instance
        session = ChatSession("Test Session", "Testing", [human])

        # Test that send_new_message raises a NotImplementedError for Human
        with self.assertRaises(NotImplementedError):
            human.send_new_message(session)

        # Create a LLMAgent instance
        llm_agent = LLMAgent("AI", "bot", Instruction("Hello"), llm_api="openai")
        session.add_attendee(llm_agent)

        # Test that send_new_message works for LLMAgent
        if USE_ACTUAL_LLM_API:
            try:
                message = llm_agent.send_new_message(session)
                self.assertEqual(session.chat_history[-1], message)
            except Exception as e:
                self.fail(f"send_new_message raised {type(e).__name__} unexpectedly!")
        else:
            if False:
                # TODO Fix this block. Mock does not work
                with patch(
                    "llm_wrap.llm_response.get_ai_response",
                    return_value="Mocked response",
                ) as mock_get_ai_response:
                    try:
                        message = llm_agent.send_new_message(session)
                        self.assertEqual(session.chat_history[-1], message)
                    except Exception as e:
                        self.fail(
                            f"send_new_message raised {type(e).__name__} unexpectedly!"
                        )

                    # Check that the mock was called
                    mock_get_ai_response.assert_called_once()


class TestLLMAgentMethods(unittest.TestCase):
    def test_convert_chat_history_to_openai_messages(self):
        # Setup
        llm_agent = LLMAgent("AI", "bot", Instruction("Hello"), llm_api="openai")
        human = Human("John", "user", Instruction("Hi"))
        chat_history = [
            Message(human, "Hi"),
            Message(llm_agent, "Hello"),
            Message(human, "How are you?"),
        ]

        # Execution
        messages = llm_agent.convert_chat_history_to_openai_messages(chat_history)

        # Verification
        self.assertEqual(
            len(messages), len(chat_history) + 1
        )  # +1 for the system message
        self.assertEqual(
            messages[0], {"role": "system", "content": llm_agent.instruction.text}
        )
        for i, message in enumerate(chat_history, start=1):
            expected_role = "user" if i % 2 == 1 else "assistant"
            self.assertEqual(
                messages[i], {"role": expected_role, "content": message.text}
            )


class TestChatSessionEndMethod(unittest.TestCase):
    def setUp(self):
        # Create a ChatSession instance
        session_init_json = _get_init_json_data()
        self.session = ChatSession(**session_init_json)

    def test_end_session(self):
        # Start the session
        self.session.start()
        self.assertEqual(self.session.status, "started")

        # End the session successfully
        self.session.end("completed_successfully", "MaxSentMessage")
        self.assertEqual(self.session.status, "completed_successfully")
        self.assertEqual(self.session.finish_reason, "MaxSentMessage")
        self.assertIsNotNone(self.session.end_at)

        # End the session with failure
        self.session.end("completed_with_failure", "LLMAPIFailure")
        self.assertEqual(self.session.status, "completed_with_failure")
        self.assertEqual(self.session.finish_reason, "LLMAPIFailure")
        self.assertIsNotNone(self.session.end_at)


class TestMessageSchema(unittest.TestCase):
    def setUp(self):
        self.message_schema = MessageSchema()
        self.attendee_schema = AttendeeSchema()
        self.instruction = Instruction("Test instruction")
        self.attendee = Human(
            "Test Attendee", "user", self.instruction
        )
        self.message = Message(self.attendee, "Test message")

    def test_serialize_message(self):
        serialized_message = self.message_schema.dump(self.message)
        expected_output = {
            "sender": self.attendee_schema.dump(self.attendee),
            "text": "Test message",
            "timestamp": self.message.timestamp.strftime("%Y-%m-%dT%H:%M:%S"),
        }
        self.assertEqual(serialized_message, expected_output)

    def test_deserialize_message(self):
        serialized_message = self.message_schema.dump(self.message)
        deserialized_message = self.message_schema.load(serialized_message)
        self.assertEqual(deserialized_message.sender.name, self.message.sender.name)
        self.assertEqual(deserialized_message.text, self.message.text)
        # Compare timestamps up to seconds
        self.assertEqual(
            deserialized_message.timestamp.replace(microsecond=0),
            self.message.timestamp.replace(microsecond=0),
        )

    def test_deserialize_invalid_message(self):
        invalid_message = {
            "sender": self.attendee_schema.dump(self.attendee),
            "text": "Test message",
            "timestamp": "invalid timestamp",
        }
        with self.assertRaises(ValidationError):
            self.message_schema.load(invalid_message)


class TestChatSessionSchema(unittest.TestCase):
    def setUp(self):
        self.chat_session_schema = ChatSessionSchema()
        self.attendee_schema = AttendeeSchema()
        self.message_schema = MessageSchema()
        self.instruction = Instruction("Test instruction")
        self.attendee = Human(
            "Test Attendee", "user", self.instruction
        )
        self.message = Message(self.attendee, "Test message")
        self.chat_session = ChatSession(
            title="Test Session",
            purpose="Testing",
            attendees=[self.attendee],
            chat_history=[self.message]
        )

    def test_serialize_chat_session(self):
        serialized_chat_session = self.chat_session_schema.dump(self.chat_session)
        expected_output = {
            'title': "Test Session",
            'purpose': "Testing",
            'attendees': [self.attendee_schema.dump(self.attendee)],
            'settings': {},
            'start_at': None,
            'updated_at': None,
            'end_at': None,
            'finish_reason': None,
            'status': "initialized",
            'chat_history': [self.message_schema.dump(self.message)]
        }
        self.assertEqual(serialized_chat_session, expected_output)

    def test_deserialize_chat_session(self):
        serialized_chat_session = self.chat_session_schema.dump(self.chat_session)
        deserialized_chat_session = self.chat_session_schema.load(serialized_chat_session)
        self.assertEqual(deserialized_chat_session.title, self.chat_session.title)
        self.assertEqual(deserialized_chat_session.purpose, self.chat_session.purpose)
        self.assertEqual(deserialized_chat_session.attendees[0].name, self.chat_session.attendees[0].name)
        self.assertEqual(deserialized_chat_session.chat_history[0].text, self.chat_session.chat_history[0].text)

    def test_deserialize_invalid_chat_session(self):
        invalid_chat_session = {
            'purpose': "Testing",
            'attendees': [self.attendee_schema.dump(self.attendee)],
            'settings': {},
            'start_at': None,
            'updated_at': None,
            'end_at': None,
            'finish_reason': None,
            'status': "initialized",
            'chat_history': [self.message_schema.dump(self.message)]
        }
        with self.assertRaises(ValidationError):
            self.chat_session_schema.load(invalid_chat_session)

class TestChatSessionFromJsonToJson(unittest.TestCase):
    def setUp(self):
        self.chat_session_schema = ChatSessionSchema()
        self.attendee_schema = AttendeeSchema()
        self.message_schema = MessageSchema()
        self.instruction = Instruction("Test instruction")
        self.attendee = Human(
            "Test Attendee", "user", self.instruction
        )
        self.message = Message(self.attendee, "Test message")
        self.chat_session = ChatSession(
            title="Test Session",
            purpose="Testing",
            attendees=[self.attendee],
            chat_history=[self.message]
        )

    def test_to_json(self):
        serialized_chat_session = self.chat_session.to_json()
        expected_output = self.chat_session_schema.dumps(self.chat_session)
        self.assertEqual(serialized_chat_session, expected_output)

    def test_from_json(self):
        serialized_chat_session = self.chat_session.to_json()
        deserialized_chat_session = ChatSession.from_json(serialized_chat_session)
        self.assertEqual(deserialized_chat_session.title, self.chat_session.title)
        self.assertEqual(deserialized_chat_session.purpose, self.chat_session.purpose)
        self.assertEqual(deserialized_chat_session.attendees[0].name, self.chat_session.attendees[0].name)
        self.assertEqual(deserialized_chat_session.chat_history[0].text, self.chat_session.chat_history[0].text)

    def test_to_dict(self):
        dict_data = self.chat_session.to_dict()
        expected_output = self.chat_session_schema.dumps(self.chat_session)
        self.assertEqual(dict_data, yaml.safe_load(expected_output))

    def test_to_yaml(self):
        yaml_data = self.chat_session.to_yaml()
        expected_output = yaml.dump(yaml.safe_load(self.chat_session_schema.dumps(self.chat_session)), default_flow_style=False)
        self.assertEqual(yaml_data, expected_output)

class TestMessage(unittest.TestCase):
    def test_create(self):
        # Test with a Human sender
        sender_name = "Test Human"
        sender_role = "user"
        sender_type = "Human"
        sender_attendee_params = {}
        text = "Hello, world!"
        message = Message.create(sender_name, sender_role, sender_type, sender_attendee_params, text)
        self.assertIsInstance(message.sender, Human)
        self.assertEqual(message.text, text)

        # Test with an LLMAgent sender
        sender_name = "Test LLMAgent"
        sender_role = "assistant"
        sender_type = "LLMAgent"
        sender_attendee_params = {"llm_api": "openai"}
        text = "Hello, user!"
        message = Message.create(sender_name, sender_role, sender_type, sender_attendee_params, text)
        self.assertIsInstance(message.sender, LLMAgent)
        self.assertEqual(message.text, text)

        # Test with an invalid sender_type
        sender_type = "InvalidType"
        with self.assertRaises(ValueError):
            message = Message.create(sender_name, sender_role, sender_type, sender_attendee_params, text)

class TestChatSession(unittest.TestCase):
    def setUp(self):
        self.instruction = Instruction("Test instruction")
        self.attendee = Human(
            "Test Attendee", "user", self.instruction
        )
        self.message = Message(self.attendee, "Test message")
        self.chat_session = ChatSession(
            title="Test Session",
            purpose="Testing",
            attendees=[self.attendee],
            chat_history=[self.message]
        )

    def test_get_message_from_history(self):
        message_dict = self.chat_session.get_message_from_history(0)
        self.assertIsInstance(message_dict, dict)
        self.assertEqual(message_dict["sender"]["name"], self.message.sender.name)
        self.assertEqual(message_dict["text"], self.message.text)

class TestChatSessionSetMaxMessages(unittest.TestCase):
    def setUp(self):
        self.chat_session = ChatSession(
            title="Test Session",
            purpose="Testing",
            attendees=[],
            chat_history=[]
        )

    def test_set_max_messages(self):
        # Set max_sent_message to a specific value
        self.chat_session.set_max_messages(10)
        self.assertEqual(self.chat_session.settings["max_sent_message"], 10)

        # Change max_sent_message to a new value
        self.chat_session.set_max_messages(20)
        self.assertEqual(self.chat_session.settings["max_sent_message"], 20)

if __name__ == '__main__':
    unittest.main()


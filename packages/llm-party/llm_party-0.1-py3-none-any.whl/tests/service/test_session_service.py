import os
import yaml
from datetime import datetime
import json
import unittest
from llm_party.service import start_session
from llm_party.service.session_service import validate_config_file, initialize_chat_session, progress_chat_session, create_first_message, start_session_with_user_first_message
from llm_party.model.session_models import ChatSession, MessageSchema, LLMAgent, Human, Message
from unittest.mock import patch, mock_open
from unittest import skipIf
original_open = open


USE_ACTUAL_LLM_API = False

def skip_if_no_api():
    return skipIf(not USE_ACTUAL_LLM_API, "Skipping this test because USE_ACTUAL_LLM_API is False")

def saved_dir():
    return './tests/service/data/saved/'


def _get_valid_config_file_path():
    return f"{service_data_path()}../../data/valid_config.json"

def _get_invalid_config_file_path():
    return f"{service_data_path()}invalid_config.json"

def service_data_path():
    return './tests/service/data/'

class TestConfigFileValidation(unittest.TestCase):
    def setUp(self):
        self.valid_config_file = _get_valid_config_file_path()
        self.invalid_config_file = _get_invalid_config_file_path()
        self.missing_fields_file1 = f"{service_data_path()}missing_fields1.json"
        self.missing_fields_file2 = f"{service_data_path()}missing_fields2.json"
        self.extra_fields_file = f"{service_data_path()}extra_fields.json"
        self.wrong_type_fields_file1 = f"{service_data_path()}wrong_type_fields1.json"
        self.wrong_type_fields_file2 = f"{service_data_path()}wrong_type_fields2.json"
        self.invalid_json_format_file = f"{service_data_path()}invalid_json_format_file.json"

    def test_valid_config_file(self):
        try:
            validate_config_file(self.valid_config_file)
        except ValueError:
            self.fail("validate_config_file() raised ValueError unexpectedly!")

    def test_invalid_config_file(self):
        with self.assertRaises(ValueError) as context:
            validate_config_file(self.invalid_config_file)
        self.assertIn("Error reading the configuration file", str(context.exception))

    def test_missing_fields_file1(self):
        with self.assertRaises(ValueError) as context:
            validate_config_file(self.missing_fields_file1)
        self.assertIn("Each LLM agent must have 'llm_api_params' field", str(context.exception))

    def test_missing_fields_file2(self):
        with self.assertRaises(ValueError) as context:
            validate_config_file(self.missing_fields_file2)
        self.assertIn("The configuration file must contain more than two agents", str(context.exception))

    def test_wrong_type_fields_file1(self):
        with self.assertRaises(ValueError) as context:
            validate_config_file(self.wrong_type_fields_file1)
        self.assertIn("'max_sent_message' must be an integer", str(context.exception))

    def test_wrong_type_fields_file2(self):
        with self.assertRaises(ValueError) as context:
            validate_config_file(self.wrong_type_fields_file2)
        self.assertIn("'max_sent_message' must be greater than 0", str(context.exception))

    def test_invalid_json_file(self):
        with self.assertRaises(ValueError) as context:
            validate_config_file(self.invalid_json_format_file)
        self.assertIn("Error reading the configuration file", str(context.exception))

    def test_file_not_exists(self):
        with self.assertRaises(ValueError) as context:
            validate_config_file("not_exists.json")
        self.assertIn("The configuration file not_exists.json does not exist or is not accessible", str(context.exception))

class TestInitializeChatSession(unittest.TestCase):
    def setUp(self):
        self.valid_config_file = _get_valid_config_file_path()
        self.invalid_config_file = _get_invalid_config_file_path()
        self.invalid_schema_config_file = 'invalid_schema_config.json'

    def test_valid_config_file(self):
        try:
            chat_session = initialize_chat_session(self.valid_config_file)
            self.assertIsInstance(chat_session, ChatSession)
        except ValueError:
            self.fail("initialize_chat_session() raised ValueError unexpectedly!")

    def test_invalid_config_file(self):
        with self.assertRaises(ValueError):
            initialize_chat_session(self.invalid_config_file)

    def test_invalid_schema_config_file(self):
        with self.assertRaises(ValueError):
            initialize_chat_session(self.invalid_schema_config_file)


class TestProgressChatSession(unittest.TestCase):
    def setUp(self):
        self.valid_config_file = _get_valid_config_file_path()

    @skip_if_no_api()
    def test_progress_chat_session_success(self):
        # Initialize a chat session with a valid configuration
        chat_session = initialize_chat_session(self.valid_config_file)
        # Progress the chat session
        chat_session, _ = progress_chat_session(chat_session, save_dir=saved_dir())
        # Check that the chat session status and finish reason are set correctly
        self.assertEqual(chat_session.status, 'completed_successfully')
        self.assertEqual(chat_session.finish_reason, 'MaxSentMessage')
        # Check that the chat history is updated correctly
        self.assertEqual(len(chat_session.chat_history), chat_session.settings['max_sent_message'])
        # Check that the end_at field is set
        self.assertIsNotNone(chat_session.end_at)

    @patch('llm_party.model.session_models.get_ai_response', return_value='Mocked response')
    def test_progress_chat_session_with_mocked_api(self, mock_get_ai_response):
        # Initialize a chat session with a valid configuration
        chat_session = initialize_chat_session(self.valid_config_file)
        # Progress the chat session
        chat_session, _ = progress_chat_session(chat_session, save_dir=saved_dir())
        # Check that the chat session status and finish reason are set correctly
        self.assertEqual(chat_session.status, 'completed_successfully')
        self.assertEqual(chat_session.finish_reason, 'MaxSentMessage')
        # Check that the chat history is updated correctly
        self.assertEqual(len(chat_session.chat_history), chat_session.settings['max_sent_message'])
        # Check that the end_at field is set
        self.assertIsNotNone(chat_session.end_at)
        # Check that the get_ai_response function was called the expected number of times
        self.assertEqual(mock_get_ai_response.call_count, chat_session.settings['max_sent_message'])

    @patch('llm_party.model.session_models.Attendee.send_new_message', side_effect=Exception('Test exception'))
    def test_progress_chat_session_failure(self, mock_send_new_message):
        # Initialize a chat session with a valid configuration
        chat_session = initialize_chat_session(self.valid_config_file)
        # Progress the chat session
        try:
            chat_session, _ = progress_chat_session(chat_session, save_dir=saved_dir())
        except Exception:
            pass
        # Check that the chat session status and finish reason are set correctly
        self.assertEqual(chat_session.status, 'completed_with_failure')
        self.assertTrue(chat_session.finish_reason.startswith('LLMAPIFailure'))

    @skip_if_no_api()
    def test_chat_session_completion_success(self):
        # Initialize a chat session with a valid configuration
        chat_session = initialize_chat_session(self.valid_config_file)
        # Progress the chat session
        chat_session, save_file_path = progress_chat_session(chat_session, save_dir=saved_dir())
        # Check that the chat session status and finish reason are set correctly
        self.assertEqual(chat_session.status, 'completed_successfully')
        self.assertEqual(chat_session.finish_reason, 'MaxSentMessage')
        # Check that the ChatSession object is correctly serialized to a JSON file
        with open(save_file_path, 'r') as f:
            saved_chat_session = json.load(f)
        self.assertEqual(saved_chat_session, chat_session.to_json())

    @patch('llm_party.model.session_models.get_ai_response', return_value='Test response')
    def test_chat_session_completion_success_with_mock(self, mock_get_ai_response):
        # Initialize a chat session with a valid configuration
        chat_session = initialize_chat_session(self.valid_config_file)
        # Progress the chat session
        chat_session, save_file_path = progress_chat_session(chat_session, save_dir=saved_dir())
        # Check that the chat session status and finish reason are set correctly
        self.assertEqual(chat_session.status, 'completed_successfully')
        self.assertEqual(chat_session.finish_reason, 'MaxSentMessage')
        # Check that the ChatSession object is correctly serialized to a JSON file
        with open(save_file_path, 'r') as f:
            saved_chat_session = json.load(f)
        self.assertEqual(saved_chat_session, json.loads(chat_session.to_json()))
        # Check that the get_ai_response function was called
        mock_get_ai_response.assert_called()

    @patch('llm_party.model.session_models.Attendee.send_new_message', side_effect=Exception('Test exception'))
    def test_chat_session_completion_failure(self, mock_send_new_message):
        # Initialize a chat session with a valid configuration
        chat_session = initialize_chat_session(self.valid_config_file)
        # Progress the chat session
        try:
            chat_session, _ = progress_chat_session(chat_session, save_dir=saved_dir())
        except Exception:
            pass
        # Check that the chat session status and finish reason are set correctly
        self.assertEqual(chat_session.status, 'completed_with_failure')
        self.assertTrue(chat_session.finish_reason.startswith('LLMAPIFailure'))

    @skip_if_no_api()
    def test_chat_session_completion_save_file_path_not_writable(self):
        def side_effect(*args, **kwargs):
            if args[0] == self.valid_config_file:
                return original_open(*args, **kwargs)
            else:
                raise PermissionError

        with patch('builtins.open', side_effect=side_effect) as mock_open:
            # Initialize a chat session with a valid configuration
            chat_session = initialize_chat_session(self.valid_config_file)
            # Progress the chat session
            with self.assertRaises(PermissionError):
                chat_session, _ = progress_chat_session(chat_session, save_dir=saved_dir())

    def side_effect_os_error(*args, **kwargs):
        if 'w' in args[1]:
            raise OSError
        return original_open(*args, **kwargs)

    @skip_if_no_api()
    @patch('builtins.open', side_effect=side_effect_os_error)
    def test_chat_session_completion_not_enough_disk_space(self, mock_open):
        # Initialize a chat session with a valid configuration
        chat_session = initialize_chat_session(self.valid_config_file)
        # Progress the chat session
        with self.assertRaises(OSError):
            chat_session, _ = progress_chat_session(chat_session, save_dir=saved_dir())

    @patch('llm_party.model.session_models.get_ai_response', return_value='Test response')
    def test_chat_session_completion_not_enough_disk_space_with_mock(self, mock_get_ai_response):
        def side_effect_os_error(*args, **kwargs):
            if 'w' in args[1]:
                raise OSError
            return original_open(*args, **kwargs)

        with patch('builtins.open', side_effect=side_effect_os_error):
            # Initialize a chat session with a valid configuration
            chat_session = initialize_chat_session(self.valid_config_file)
            # Progress the chat session
            with self.assertRaises(OSError):
                chat_session, _ = progress_chat_session(chat_session, save_dir=saved_dir())

    @patch('llm_party.model.session_models.get_ai_response', return_value='Test response')
    def test_chat_session_completion_save_file_path_not_writable_with_mock(self, mock_get_ai_response):
        def side_effect(*args, **kwargs):
            if args[0] == self.valid_config_file:
                return original_open(*args, **kwargs)
            else:
                raise PermissionError

        with patch('builtins.open', side_effect=side_effect):
            # Initialize a chat session with a valid configuration
            chat_session = initialize_chat_session(self.valid_config_file)
            # Progress the chat session
            with self.assertRaises(PermissionError):
                chat_session, _ = progress_chat_session(chat_session, save_dir=saved_dir())


class TestStartSession(unittest.TestCase):
    def setUp(self):
        self.valid_config_file_path = _get_valid_config_file_path()
        self.invalid_config_file_path = _get_invalid_config_file_path()
        self.save_dir = saved_dir()
        self.save_file_name = "test_chat_session.json"

    @skip_if_no_api()
    def test_start_session_valid_config(self):
        chat_session, saved_file_path = start_session(self.valid_config_file_path, save_dir=self.save_dir, save_file_name=self.save_file_name)
        self.assertIsInstance(chat_session, ChatSession)
        self.assertEqual(chat_session.status, 'completed_successfully')
        self.assertEqual(saved_file_path, os.path.join(self.save_dir, self.save_file_name))

    def test_start_session_invalid_config(self):
        # Test start_session with an invalid configuration file
        with self.assertRaises(ValueError):
            start_session(self.invalid_config_file_path, save_dir=self.save_dir, save_file_name=self.save_file_name)

    @patch('llm_party.service.session_service.progress_chat_session', side_effect=Exception('Test exception'))
    def test_start_session_failed_chat(self, mock_progress_chat_session):
        # Test start_session with a valid configuration file that causes the chat to fail
        with self.assertRaises(Exception) as context:
            start_session(self.valid_config_file_path, save_dir=self.save_dir, save_file_name=self.save_file_name)
        self.assertEqual(str(context.exception), 'Test exception')

    @patch('llm_party.model.session_models.get_ai_response', return_value='Mocked response')
    def test_start_session_valid_config_with_mock(self, mock_get_ai_response):
        # Test start_session with a valid configuration file
        chat_session, saved_file_path = start_session(self.valid_config_file_path, save_dir=self.save_dir, save_file_name=self.save_file_name)
        self.assertIsInstance(chat_session, ChatSession)
        self.assertEqual(chat_session.status, 'completed_successfully')
        self.assertEqual(saved_file_path, os.path.join(self.save_dir, self.save_file_name))

    @patch('llm_party.model.session_models.get_ai_response', return_value='Mocked response')
    def test_start_session_invalid_config_with_mock(self, mock_get_ai_response):
        # Test start_session with an invalid configuration file
        with self.assertRaises(ValueError):
            start_session(self.invalid_config_file_path, save_dir=self.save_dir, save_file_name=self.save_file_name)

    @patch('llm_party.service.session_service.progress_chat_session', side_effect=Exception('Test exception'))
    def test_start_session_failed_chat_with_mock(self, mock_progress_chat_session):
        # Test start_session with a valid configuration file that causes the chat to fail
        with self.assertRaises(Exception) as context:
            start_session(self.valid_config_file_path, save_dir=self.save_dir, save_file_name=self.save_file_name)
        self.assertEqual(str(context.exception), 'Test exception')

    @patch('llm_party.model.session_models.get_ai_response', return_value='Mocked response')
    def test_start_session_save_as_yaml(self, mock_get_ai_response):
        # Test start_session with save_yaml=True
        chat_session, saved_file_path = start_session(
            self.valid_config_file_path, 
            save_dir=self.save_dir, 
            save_file_name=self.save_file_name, 
            save_yaml=True
        )
        self.assertIsInstance(chat_session, ChatSession)
        self.assertEqual(chat_session.status, 'completed_successfully')
        self.assertEqual(saved_file_path, os.path.join(self.save_dir, self.save_file_name))
        # Check if the saved file is a valid YAML file
        with open(saved_file_path, 'r') as f:
            try:
                yaml.safe_load(f)
            except yaml.YAMLError:
                self.fail("The saved file is not a valid YAML file.")

    def tearDown(self):
        # Teardown code here
        pass


class TestSessionService(unittest.TestCase):
    def test_create_first_message(self):
        # Test with a Human sender
        sender_name = "Test Human"
        sender_role = "user"
        sender_type = "Human"
        sender_attendee_params = {}
        text = "Hello, world!"
        serialized_message = create_first_message(sender_name, sender_role, sender_type, sender_attendee_params, text)
        message_schema = MessageSchema()
        message = message_schema.load(serialized_message)
        self.assertIsInstance(message.sender, Human)
        self.assertEqual(message.text, text)

        # Test with an LLMAgent sender
        sender_name = "Test LLMAgent"
        sender_role = "assistant"
        sender_type = "LLMAgent"
        sender_attendee_params = {"llm_api": "openai"}
        text = "Hello, user!"
        serialized_message = create_first_message(sender_name, sender_role, sender_type, sender_attendee_params, text)
        message = message_schema.load(serialized_message)
        self.assertIsInstance(message.sender, LLMAgent)
        self.assertEqual(message.text, text)

        # Test with an invalid sender_type
        sender_type = "InvalidType"
        with self.assertRaises(ValueError):
            serialized_message = create_first_message(sender_name, sender_role, sender_type, sender_attendee_params, text)

    @patch('llm_party.model.session_models.get_ai_response', return_value='Mocked response')
    def test_start_session_with_user_first_message_with_mock(self, mock_get_ai_response):
        # Test with a Human sender
        config_file_path = _get_valid_config_file_path()
        first_message = "Hello, world!"
        sender_name = "Test Human"
        sender_role = "user"
        sender_type = "Human"
        sender_attendee_params = {}
        save_dir = None
        save_file_name = None

        chat_session, saved_file_path = start_session_with_user_first_message(
            config_file_path, first_message, sender_name, sender_role, sender_type, sender_attendee_params, save_dir, save_file_name
        )

        self.assertIsInstance(chat_session, ChatSession)
        self.assertEqual(len(chat_session.chat_history), 2)
        self.assertIsInstance(chat_session.chat_history[0], Message)
        self.assertEqual(chat_session.chat_history[0].text, first_message)

    @skip_if_no_api()
    def test_start_session_with_user_first_message(self, mock_get_ai_response):
        # Test with a Human sender
        config_file_path = _get_valid_config_file_path()
        first_message = "Hello, world!"
        sender_name = "Test Human"
        sender_role = "user"
        sender_type = "Human"
        sender_attendee_params = {}
        save_dir = None
        save_file_name = None

        chat_session, saved_file_path = start_session_with_user_first_message(
            config_file_path, first_message, sender_name, sender_role, sender_type, sender_attendee_params, save_dir, save_file_name
        )

        self.assertIsInstance(chat_session, ChatSession)
        self.assertEqual(len(chat_session.chat_history), 2)
        self.assertIsInstance(chat_session.chat_history[0], Message)
        self.assertEqual(chat_session.chat_history[0].text, first_message)


if __name__ == "__main__":
    unittest.main()
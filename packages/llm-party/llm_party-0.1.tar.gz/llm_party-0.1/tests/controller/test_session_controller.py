from typing import Literal
import unittest
from unittest import skipIf
import os
from unittest.mock import patch, MagicMock
from llm_party.controller.session_controller import start_session_with_first_message_controller, start_session_controller, ChatSession
from llm_party.service.session_service import initialize_chat_session

USE_ACTUAL_LLM_API = False


def test_data_path():
    return './tests/data/'

def _get_valid_config_file_path():
    return f"{test_data_path()}valid_config.json"


def skip_if_no_api():
    return skipIf(not USE_ACTUAL_LLM_API, "Skipping this test because USE_ACTUAL_LLM_API is False")

class TestSessionController(unittest.TestCase):
    @skip_if_no_api()
    def test_start_session_with_first_message_controller_with_yaml(self):
        # Define the path to the sample YAML file
        yaml_file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'initial_config_sample.yaml')

        # Define the parameters for the function
        first_message = "Hello, world!"
        sender_name = "Test Sender"
        sender_role = "user"
        sender_type = "Human"
        sender_attendee_params = {}

        # Call the function
        start_session_with_first_message_controller(yaml_file_path, first_message, sender_name, sender_role, sender_type, sender_attendee_params)

        # If the function completes without raising an exception, the test passes
        self.assertTrue(True)

    @patch('llm_party.controller.session_controller.start_session')
    def test_start_session(self, mock_start_session):
        # Arrange
        config_file_path = 'test_config.json'
        save_dir = 'test_dir'
        save_file_name = 'test_file'
        pretty_print = False
        save_yaml = False
        mock_start_session.return_value = (MagicMock(), 'mocked_file_path')
        output = None

        # Act
        start_session_controller(config_file_path, save_dir, save_file_name, pretty_print, save_yaml, output)

        # Assert
        mock_start_session.assert_called_once_with(config_file_path, save_dir, save_file_name, pretty_print, save_yaml, output)

    @patch('llm_party.model.session_models.get_ai_response', return_value='Mocked response')
    def test_start_session_with_first_message_controller_with_yaml_with_mock(self, mock_get_ai_response):
        # Define the path to the sample YAML file
        yaml_file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'initial_config_sample.yaml')

        # Define the parameters for the function
        first_message = "Hello, world!"
        sender_name = "Test Sender"
        sender_role = "user"
        sender_type = "Human"
        sender_attendee_params = {}

        # Call the function
        start_session_with_first_message_controller(yaml_file_path, first_message, sender_name, sender_role, sender_type, sender_attendee_params)

        # If the function completes without raising an exception, the test passes
        self.assertTrue(True)

    @patch('llm_party.controller.session_controller.start_session')
    def test_start_session_with_yaml(self, mock_start_session):
        # Arrange
        config_file_path = 'test_config.json'
        save_dir = 'test_dir'
        save_file_name = 'test_file'
        pretty_print = False
        save_yaml = True
        output = None

        mock_start_session.return_value = (MagicMock(), 'mocked_file_path')

        # Act
        start_session_controller(config_file_path, save_dir, save_file_name, pretty_print, save_yaml, output)

        # Assert
        mock_start_session.assert_called_once_with(config_file_path, save_dir, save_file_name, pretty_print, save_yaml, output)

    @patch('llm_party.model.session_models.get_ai_response', return_value='Mocked response')
    def test_start_session_with_first_message_controller_with_yaml_with_mock(self, mock_get_ai_response):
        # Define the path to the sample YAML file
        yaml_file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'initial_config_sample.yaml')

        # Define the parameters for the function
        first_message = "Hello, world!"
        sender_name = "Test Sender"
        sender_role = "user"
        sender_type = "Human"
        sender_attendee_params = {}
        save_yaml = True

        # Call the function
        start_session_with_first_message_controller(yaml_file_path, first_message, sender_name, sender_role, sender_type, sender_attendee_params, save_yaml=save_yaml)

        # If the function completes without raising an exception, the test passes
        self.assertTrue(True)

    @patch('os.remove')
    @patch('tempfile.NamedTemporaryFile')
    @patch('llm_party.controller.session_controller.start_session')
    def test_start_session_controller_with_dict(self, mock_start_session, mock_temp_file, mock_os_remove):
        mock_file = MagicMock()
        mock_file.name = 'temp.json'
        mock_temp_file.return_value = mock_file
        mock_start_session.return_value = (MagicMock(), 'mocked_file_path')
        config = {"key": "value"}
        output = None

        start_session_controller(config)

        mock_start_session.assert_called_once_with('temp.json', None, None, False, False, output)

    @patch('os.remove')
    @patch('tempfile.NamedTemporaryFile')
    @patch('llm_party.controller.session_controller.start_session_with_user_first_message')
    def test_start_session_with_first_message_controller_with_dict(self, mock_start_session, mock_temp_file, mock_os_remove):
        # Arrange
        mock_file = MagicMock()
        mock_file.name = 'temp.json'
        mock_temp_file.return_value = mock_file

        first_message: str = "Hello, world!"
        sender_name: str = "Test Sender"
        sender_role: str = "user"
        sender_type: Literal["Human", "Agent"] = "Human"
        sender_attendee_params: dict = {}
        output = None

        config = {"key": "value"}

        mock_start_session.return_value = (MagicMock(), 'mocked_file_path')

        # Act
        start_session_with_first_message_controller(config, first_message, sender_name, sender_role, sender_type, sender_attendee_params, output)

        # Assert
        mock_start_session.assert_called_once_with(
            'temp.json', first_message, sender_name, sender_role, sender_type, sender_attendee_params,
            None, None, False, False, output)

    @patch('os.remove')
    @patch('tempfile.NamedTemporaryFile')
    @patch('llm_party.controller.session_controller.start_session')
    def test_start_session_controller_with_chat_session(self, mock_start_session, mock_temp_file, mock_os_remove):
        mock_file = MagicMock()
        mock_file.name = 'temp.json'
        mock_temp_file.return_value = mock_file
        mock_start_session.return_value = (MagicMock(), 'mocked_file_path')

        chat_session = initialize_chat_session(_get_valid_config_file_path())
        # config = ChatSession.from_json(_get_valid_config_file_path())
        start_session_controller(chat_session)

        mock_start_session.assert_called_once_with('temp.json', None, None, False, False, None)

    @patch('os.remove')
    @patch('tempfile.NamedTemporaryFile')
    @patch('llm_party.controller.session_controller.start_session_with_user_first_message')
    def test_start_session_with_first_message_controller_with_chat_session(self, mock_start_session, mock_temp_file, mock_os_remove):
        mock_file = MagicMock()
        mock_file.name = 'temp.json'
        mock_temp_file.return_value = mock_file
        mock_start_session.return_value = (MagicMock(), 'mocked_file_path')
        # Define the parameters for the function
        first_message = "Hello, world!"
        sender_name = "Test Sender"
        sender_role = "user"
        sender_type = "Human"
        sender_attendee_params = {}
        config = ChatSession()

        start_session_with_first_message_controller(config, first_message, sender_name, sender_role, sender_type, sender_attendee_params)

        mock_start_session.assert_called_once_with('temp.json', first_message, sender_name, sender_role, sender_type, sender_attendee_params, None, None, False, False, None)


if __name__ == '__main__':
    unittest.main()
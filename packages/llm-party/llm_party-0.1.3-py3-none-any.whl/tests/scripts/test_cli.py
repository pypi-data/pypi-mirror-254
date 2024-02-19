import unittest
from unittest.mock import patch
from llm_party.scripts import cli

class TestCLI(unittest.TestCase):
    @patch('llm_party.scripts.cli.start_session_controller')
    def test_start_session_mode(self, mock_start_session_controller):
        # test_args = ['--mode', 'start', '--config_file_path', 'test_config.json']
        test_args = ['dummy_script_name', '--mode', 'start', '--config_file_path', 'test_config.json']
        with patch.object(cli.sys, 'argv', test_args):
            try:
                cli.main()
            except SystemExit as e:
                self.fail(f"SystemExit was raised: {e}")
        mock_start_session_controller.assert_called_once_with('test_config.json', None, None)

    @patch('llm_party.scripts.cli.start_session_with_first_message_controller')
    def test_start_with_first_message_mode(self, mock_start_session_with_first_message_controller):
        test_args = ['dummy_script_name', '--mode', 'start_with_first_message', '--config_file_path', 'test_config.json', '--first_message', 'Hello, world!', '--sender_name', 'Test User', '--sender_role', 'user', '--sender_type', 'Human', '--sender_attendee_params', '{}']
        with patch.object(cli.sys, 'argv', test_args):
            try:
                cli.main()
            except SystemExit as e:
                self.fail(f"SystemExit was raised: {e}")
        mock_start_session_with_first_message_controller.assert_called_once_with('test_config.json', 'Hello, world!', 'Test User', 'user', 'Human', '{}', None, None)

if __name__ == '__main__':
    unittest.main()
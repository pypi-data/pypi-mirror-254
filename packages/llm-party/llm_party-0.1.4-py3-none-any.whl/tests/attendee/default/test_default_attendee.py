import unittest
from llm_party.model.session_models import ChatSession
from llm_party.attendee.default.default_attendee import RawLLMAgent, FacilitatorAgent

def _get_RawLLMAgent_config():
    return "./tests/data/valid_RawLLMAgent_config.json"

def _get_RawLLMAgent_config_json():
    config_file = _get_RawLLMAgent_config()
    with open(config_file, 'r') as f:
        json_string = f.read()
    return json_string

class TestDefaultAttendee(unittest.TestCase):
    def setUp(self):
        json_string = _get_RawLLMAgent_config_json()
        chat_session = ChatSession.from_json(json_string)
        self.raw_agent = chat_session.attendees[0]
        self.facilitator_agent = chat_session.attendees[1]

    def test_raw_agent_has_default_character(self):
        self.assertTrue(self.raw_agent.has_character('default'))

    def test_facilitator_agent_has_characters(self):
        self.assertTrue(self.facilitator_agent.has_character('introduce_oneself'))
        self.assertTrue(self.facilitator_agent.has_character('can_terminate'))
        self.assertTrue(self.facilitator_agent.has_character('is_good_at_communication'))

    def test_raw_agent_gives_character_instruction(self):
        self.assertEqual(self.raw_agent.trait_instruction()[0:18], "## Additional Rule")

    def test_facilitator_agent_gives_character_instruction(self):
        self.assertEqual(self.facilitator_agent.trait_instruction()[0:18], "## Additional Rule")

    def test_raise(self):
        class InvalidAgent(RawLLMAgent):
            pass


class TestRawLLMAgentFromJson(unittest.TestCase):
    def test_from_json(self):
        json_string = _get_RawLLMAgent_config_json()
        try:
            chat_session = ChatSession.from_json(json_string)
        except Exception as e:
            self.fail(f"Test failed with exception: {e}")

        self.assertEqual(chat_session.attendees[0].llm_api, "openai")

if __name__ == '__main__':
    unittest.main()
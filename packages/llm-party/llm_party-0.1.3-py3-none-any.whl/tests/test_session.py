import unittest
from unittest.mock import patch
from llm_party import session

class TestSession(unittest.TestCase):

    def test_create_session(self):
        # Arrange

        # Act
        result = session.create_session(llm_api="openai")

        # Assert
        self.assertEqual(result, 'Temp response')

if __name__ == '__main__':
    unittest.main()
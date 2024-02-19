import os
import unittest
from unittest.mock import patch, MagicMock
from maldinio_ai.nlp import NLPClient  # Adjust the import path as necessary
# from maldinio_ai.api.api_key_loader import OpenAIKeyLoader  # Uncomment if used

# Mock API response content
mock_response_content = "The 2020 World Series was played in Texas at Globe Life Field in Arlington."

# Creating a mock ChatCompletion object
mock_chat_completion = MagicMock()
mock_chat_completion.choices = [
    MagicMock(message=MagicMock(content=mock_response_content))
]

class TestNLPClient(unittest.TestCase):

    @patch('maldinio_ai.nlp.nlp_client.OpenAI')  # Adjust the patch location to where OpenAI is imported in your module
    def test_process_single_prompt(self, mock_openai):
        # Set up the mock to return a mock chat completion object when completions.create is called
        mock_openai_instance = mock_openai.return_value
        mock_openai_instance.chat.completions.create.return_value = mock_chat_completion

        # Create an instance of NLPClient
        nlp_client = NLPClient()

        # Test single prompt processing
        prompt = "Translate the following text into French: 'Hello, how are you?'"
        role = "assistant"
        response = nlp_client.process(prompt, role)

        # Check if the OpenAI API was called with the correct arguments
        mock_openai_instance.chat.completions.create.assert_called_once_with(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": role},
                {"role": "user", "content": prompt}
            ]
        )

        # Check if the response matches the expected result
        self.assertEqual(response, mock_response_content)

    @patch('maldinio_ai.nlp.nlp_client.OpenAI')  # Adjust the patch location to where OpenAI is imported in your module
    def test_process_conversation(self, mock_openai):
        # Set up the mock to return a mock chat completion object when completions.create is called
        mock_openai_instance = mock_openai.return_value
        mock_openai_instance.chat.completions.create.return_value = mock_chat_completion

        # Create an instance of NLPClient
        nlp_client = NLPClient()

        # Test single prompt processing
        conversation = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Translate the following text into Spanish: 'Good morning.'"}
        ]
        role = "assistant"
        response = nlp_client.process(conversation, role)

        # Check if the OpenAI API was called with the correct arguments
        mock_openai_instance.chat.completions.create.assert_called_once_with(
            model="gpt-3.5-turbo",
            messages=conversation  # Ensure the conversation is properly formatted
        )

        # Check if the response matches the expected result
        self.assertEqual(response, mock_response_content)

if __name__ == '__main__':
    # Load environment variables and API keys
    # dotenv_path = os.path.join(os.getcwd(), ".env") # Ensure your .env file is in the current working directory
    # key_loader = OpenAIKeyLoader(dotenv_path=dotenv_path)
    # api_key = key_loader.get_api_key()
    unittest.main()



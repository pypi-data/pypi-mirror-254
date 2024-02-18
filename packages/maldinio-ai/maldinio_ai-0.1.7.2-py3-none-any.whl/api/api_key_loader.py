import os
import logging
from dotenv import load_dotenv

class OpenAIKeyLoader:
    def __init__(self, dotenv_path=None):

        # Check if the .env file exists before trying to load it
        if dotenv_path is None or not os.path.exists(dotenv_path):
            raise FileNotFoundError(f"The .env file was not found at {dotenv_path}")

        # Load environment variables from the .env file
        load_dotenv(dotenv_path)

        # Get the OpenAI API Key
        self.api_key = os.environ.get("OPENAI_API_KEY")

        try:
            api_key = os.environ.get('OPENAI_API_KEY')
            if not api_key:
                raise ValueError("API key not found in .env file.")
            self.api_key = api_key
            logging.info("API Key loaded successfully.")
        except Exception as e:
            logging.error(f"Error loading API key: {e}. Please check the .env file.")
            raise

    def get_api_key(self):
        return self.api_key

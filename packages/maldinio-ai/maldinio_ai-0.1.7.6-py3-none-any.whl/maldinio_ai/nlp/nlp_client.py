import time
import logging
import os
import json
import openai
from openai import OpenAIError, APIError, RateLimitError, AuthenticationError, BadRequestError
from openai import OpenAI
from openai.types.chat import ChatCompletion

GPT_MODEL = "gpt-4-turbo"
GPT_MODEL = "gpt-3.5-turbo"  # Assuming the latest model you want to use

RETRY_COUNT = 0
MAX_RETRIES = 50  # Maximum number of retries
INITIAL_WAIT_TIME = 5  # Initial wait time in seconds

class NLPClient:
    def __init__(self, gpt_model=GPT_MODEL):
        self.gpt_model = gpt_model
        self.client = OpenAI()

    def process(self, messages, role, use_json_completion=False):
        """
        Process a single prompt or a conversation.
        
        Parameters:
        - messages: A single string (prompt) or a list of dictionaries for a conversation.
        - role: Default role for single prompt processing.
        """
        client = self.client
        payload_messages = []
        retry_count = RETRY_COUNT
        wait_time = INITIAL_WAIT_TIME

        # Check if input is a single prompt or a conversation
        if isinstance(messages, str):
            # Single prompt, construct payload with system and user roles
            payload_messages.append({"role": "system", "content": role})
            payload_messages.append({"role": "user", "content": messages})
        elif isinstance(messages, list):
            # Conversation, assume messages is a list of dictionaries
            payload_messages.extend(messages)
        else:
            raise ValueError("Unsupported message format. Expecting a string or a list of dictionaries.")

        while retry_count < MAX_RETRIES:
            try:
                if use_json_completion:
                    completion : ChatCompletion = client.chat.completions.create(
                        model=self.gpt_model,
                        completion_format={"type": "json_object"},
                        messages=payload_messages
                    )
                    response = completion.choices[0].message.content
                    return json.loads(response)  # Adjust if needed
                else:
                    completion : ChatCompletion = self.client.chat.completions.create(
                        model=self.gpt_model,
                        messages=payload_messages
                    )
                    response = completion.choices[0].message.content
                    return response

            except RateLimitError as e:
                logging.error(f"Rate limit exceeded: {e}")
                print(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
                wait_time *= 2  # Exponential backoff

            except (AuthenticationError, BadRequestError) as e:
                logging.error(f"Non-retryable error occurred: {e}")
                break  # These errors are unlikely to be resolved by retrying

            except APIError as e:
                logging.error(f"API error: {e}")
                print(f"Retrying in {wait_time} seconds...")
                time.sleep(wait_time)
                wait_time *= 2  # Exponential backoff

            except Exception as e:
                logging.error(f"Unexpected error: {e}")
                break  # Break on unexpected errors

            finally:
                retry_count += 1

        return "Error processing prompt. Please check the logs for more details."

    def to_json(self):
        # Serialize the NLPClient object to JSON
        return json.dumps({"class": "NLPClient", "gpt_model": self.gpt_model})

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls(gpt_model=data.get("gpt_model", GPT_MODEL))

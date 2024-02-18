import time
import logging
import tiktoken
import os
import json
import openai
from openai import OpenAI

GPT_MODEL = "gpt-4-1106-preview"
GPT_MODEL = "gpt-3.5-turbo-1106"

RETRY_COUNT = 0
MAX_RETRIES = 50
WAIT_TIME = 5

class NLPClient:
    def __init__(self):
        pass

    def process(self, prompt, role):
        client = OpenAI()
        retry_count = RETRY_COUNT
        wait_time = WAIT_TIME


        while retry_count < MAX_RETRIES:
            try:
                #Make your OpenAI API request here
                response = client.chat.completions.create(
                    model=GPT_MODEL,
                    messages=[
                        {"role": "system", "content": role},
                        {"role": "user", "content": prompt},
                    ]
                )
                break

            except openai.APIError as e:
                logging.error(f"OpenAI API Error: {str(e)}")
                wait_time += 5
                print(f"OpenAI: Retrying in {wait_time} seconds, retry count: {retry_count}...")
                time.sleep(wait_time)
                retry_count += 1
                
            except openai.APIConnectionError as e:
                logging.error(f"OpenAI API Connection Error: {str(e)}")
                wait_time += 5
                print(f"OpenAI: Retrying in {wait_time} seconds, retry count: {retry_count}...")
                time.sleep(wait_time)
                retry_count += 1

            except openai.APITimeoutError as e:
                logging.error(f"OpenAI Timeout Error: {str(e)}")
                wait_time += 5
                print(f"OpenAI: Retrying in {wait_time} seconds, retry count: {retry_count}...")
                time.sleep(wait_time)
                retry_count += 1

            except openai.RateLimitError as e:
                logging.error(f"OpenAI Rate Limit Error (You have hit your assigned rate limit): {str(e)}")
                wait_time += 5
                print(f"OpenAI: Retrying in {wait_time} seconds, retry count: {retry_count}...")
                time.sleep(wait_time)
                retry_count += 1
                
            except openai.InternalServerError as e:
                logging.error(f"OpenAI Internal Server Error: {str(e)}")
                wait_time += 5
                print(f"OpenAI: Retrying in {wait_time} seconds, retry count: {retry_count}...")
                time.sleep(wait_time)
                retry_count += 1
                                
            except openai.AuthenticationError as e:
                logging.error(f"OpenAI Authentication Error: {str(e)}")
                break
            
            except openai.BadRequestError as e:
                logging.error(f"OpenAI Bad Request Error (Your request was malformed or missing some required parameters, such as a token or an input): {str(e)}")
                break
            
            except openai.ConflictError as e:
                logging.error(f"OpenAI Conflict Error (The resource was updated by another request): {str(e)}")
                break
            
            except openai.NotFoundError as e:
                logging.error(f"OpenAI Not Found Error (Requested resource does not exist.): {str(e)}")
                break
            
            except openai.PermissionDeniedError as e:
                logging.error(f"OpenAI Permission Denied Error (You don't have access to the requested resource.): {str(e)}")
                break
                        
            except openai.UnprocessableEntityError as e:
                logging.error(f"OpenAI Unprocessable Entity Error (Unable to process the request despite the format being correct): {str(e)}")
                break
            
            except Exception as e:
                logging.error(f"Unexpected Error: {str(e)}")
                wait_time += 5
                print(f"OpenAI: Retrying in {wait_time} seconds, retry count: {retry_count}...")
                time.sleep(wait_time)
                retry_count += 10
                
            retry_count += 1

        response = response.choices[0].message.content
        
        print ("prompt processed by NLPClient")
        
        return response

    def process_as_json(self, prompt, role):
        client = OpenAI()

        response = client.chat.completions.create(
            model="gpt-4-1106-preview",
            response_format={ "type": "json_object" },
            messages=[
                {"role": "system", "content": role},
                {"role": "user", "content": prompt},
            ]
        )

        return response.choices[0].message.content

    def to_json(self):
        # Serialize the NLPClient object to JSON.
        # Note: since this class does not contain any dynamic data, 
        # we return a basic representation.
        return json.dumps({"class": "NLPClient"})

    @classmethod
    def from_json(cls, json_str):
        # Deserialize the JSON string back to an NLPClient object.
        # Since there's no dynamic data, we simply return a new instance.
        return cls()
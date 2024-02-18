import json
import os
from datetime import datetime
from .nlp_client import NLPClient
from ai.utils import extract_json_from_message, extract_json_string_from_message, cleanup_json_response
from ai.utils import fill_gaps_with_underscore, verify_json
from typing import List
from ai.memory_management import ModuleMemory

class NLPProcessor:
    def __init__(self, memory: ModuleMemory = None, nlp_client: NLPClient = None, project_path=None, prompt_path=None, response_path=None):
        self.memory = memory
        self.nlp_client = nlp_client if nlp_client else NLPClient()
        self.project_path = self.memory.read(["project", "files", "project_folder"])
        self.prompt_path = self.memory.read(["project", "files", "prompt_folder"])
        self.response_path = self.memory.read(["project", "files", "response_folder"])
        self.output_path = self.memory.read(["project", "files", "output_folder"])
        self.counter = 0

    def set_project_path(self, project_path):
        self.project_path = project_path

    def set_prompt_path(self, prompt_path):
        self.prompt_path = prompt_path

    def set_response_path(self, response_path):
        self.response_path = response_path

    def process(self, prompt, context):
        """Process the query using the NLP system."""

        role = context.role or "GPT Manager"
        prompt = prompt
        response_format = context.response_format or "json"
        response_structure = context.response_structure or """{ "data" : { "response" : "str" }}"""

        response = self.get_response(role, prompt, response_format, response_structure, "", True)
        #### response = self.nlp_client.process(query)

        content = self.process_response(response)

        return content

    def save_item(self, role, toggle, file_suffix, item):
        # Save item to a text file
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"{toggle}_{self.counter}_{role}{file_suffix}_{timestamp}.md"

        if toggle == "Prompt":
            save_folder = self.prompt_path
        elif toggle == "Response":
            save_folder = self.response_path
        else:
            save_folder = self.project_path
            
        print ("save_folder: ", save_folder)
        print ("filename: ", filename)
        file_path = os.path.join(save_folder, filename)

        with open(file_path, "w") as file:
            file.write(f"### {toggle} (time: {timestamp})\n\n")
            file.write(item)
            

    def get_verified_response_single(self, role, prompt: str, response_format, response_structure) -> str:
        retries = 10
        
        output_path = self.memory.read(["project", "files", "output_folder"])
        
        while retries > 0:

            # Call the GPT-4 model for each prompt and get the response
            original_response = self.nlp_client.process(prompt, role)
            
            response = cleanup_json_response(original_response)
            
            ##### response_structure = response_structure.replace('bool', 'True')

            # Save failed response as a .md file
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

            file_name = "__response_collection_" + timestamp + ".md"
            output_filename = os.path.join(self.output_path, file_name)
            
            original_file_name = "__response_original_collection_" + timestamp + ".md"
            original_output_filename = os.path.join(self.output_path, original_file_name)
            
            try :
                with open(original_output_filename, "w") as f:
                    f.write(original_response)
                with open(output_filename, "w") as f:
                    f.write(response)
            except:
                print ()
                print ()
                print ("--------------------------------")
                print ("failed to write response to file")
                print ("--------------------------------")
                print ()
                print ()
                print ("original_response: ", original_response)
                print ("--------------------------------")
                print ()
                print ()
                print ("response: ", response)
                print ("--------------------------------")
                print ()
                print ()
                pass
            
            if response_format == "markdown":
                return response
            
            # Verify the response against the JSON structure
            if verify_json(response, response_structure):
                return response
            
            print ("response verification failed, retries left: ", retries)
            # input ("press enter to continue")

            retries -= 1
        
        self.safe_error_prompt(prompt, role, response, response_structure)
        # If verification fails after all retries, raise an exception or handle it as needed
        raise Exception("Response verification failed after retries.")

    def safe_error_prompt(self, prompt, role_name, response, response_structure):

        # Save failed prompt as a .md file
        file_name = "__failed_prompt_" + role_name + ".md"
        output_filename = os.path.join(self.output_path, file_name)
        with open(output_filename, "w") as f:
            f.write(prompt)

        # Save failed response as a .md file
        file_name = "__failed_response_" + role_name + ".md"
        output_filename = os.path.join(self.output_path, file_name)
        with open(output_filename, "w") as f:
            f.write(response)

        # Save failed structure as a .md file
        file_name = "__failed__structure_" + role_name + ".md"
        output_filename = os.path.join(self.output_path, file_name)
        
        if isinstance(response_structure, dict):
            response_structure = json.dumps(response_structure)
            
        with open(output_filename, "w") as f:
            f.write(response_structure)

    

    def get_verified_response(self, role, prompts: List[str], response_format, response_structure) -> str:
        """
        Sends the prompt array to the GPT model for verification and receives verification feedback
        """
        responses = []
        
        i = 0
        role_name = fill_gaps_with_underscore(role)
        for prompt in prompts:
            i += 1

            print(f"{role} is working on: prompt {i} of {len(prompts)}")
            verified_response = self.get_verified_response_single(role, prompt, response_format, response_structure)

            # Save verification results as a .md file
            file_name = "prompt_" + role_name + ".md"
            file_name = file_name.replace("..", ".")
            output_filename = os.path.join(self.project_path, "output", file_name)
            with open(output_filename, "w") as f:
                f.write(prompt)

            # Save verification results as a .md file
            file_name = "response_" + role_name + ".md"
            file_name = file_name.replace("..", ".")
            output_filename = os.path.join(self.project_path, "output", file_name)
            with open(output_filename, "w") as f:
                f.write(verified_response)


            responses.append(verified_response)

        return "\n".join(responses)
    
    
    def submit_prompt(self, nlp_client, prompttext, role = "You are a award winning web developer", response_format = "json", response_structure = ""):
        # Use the get_verified_response method of your GPTModel class to send the prompttext for verification
        response = self.get_verified_response(role , [prompttext], response_format, response_structure)
        return response

    def init_folders(self):
        self.project_path = self.memory.read(["project", "files", "project_folder"])
        self.prompt_path = self.memory.read(["project", "files", "prompt_folder"])
        self.response_path = self.memory.read(["project", "files", "response_folder"])
        self.output_path = self.memory.read(["project", "files", "output_folder"])


    def get_response(self, role, prompt, response_format, response_structure = "", item_number = '', extract_json = True):
        
        self.init_folders()
        
        if item_number == '':
            file_suffix = ''
        else:
            file_suffix = "_" + item_number
        
        # Save prompt to a text file
        self.save_item(role, "Prompt", file_suffix, prompt)

        # Generate response
        response = self.submit_prompt(self.nlp_client, prompt, role, response_format, response_structure)
        
        if extract_json and response_format == "json": 
            response = extract_json_string_from_message(response)

        # Save response to a text file
        self.save_item(role, "Response", file_suffix, response)

        self.counter += 1

        return response
    
    def process_response(self, response):
        # Implement your response processing logic here
        processed_response = response  # Placeholder implementation, modify as needed
        return processed_response
    
    def to_json(self):
        # Serialize the NLPProcessor object to JSON.
        # This includes the serialization of the NLPClient.
        return json.dumps({
            "class": "NLPProcessor",
            "nlp_client": self.nlp_client.to_json()
        })

    @classmethod
    def from_json(cls, json_str):
        # Deserialize the JSON string back to an NLPProcessor object.
        data = json.loads(json_str)
        nlp_client = NLPClient.from_json(data["nlp_client"])
        return cls(nlp_client=nlp_client)

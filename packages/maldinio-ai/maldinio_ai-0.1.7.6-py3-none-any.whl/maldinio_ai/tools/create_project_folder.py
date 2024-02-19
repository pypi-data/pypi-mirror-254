import os
import json
from datetime import datetime
from maldinio_ai.memory_management import ModuleMemory
from maldinio_ai.nlp import NLPProcessor

class CreateProjectFolder:
    def __init__(self, memory: ModuleMemory):
        self.main_key = "project"
        self.key = "files"
        self.sub_key = "project_folder"
        self.memory = memory
        self.root_folder = "temp_project"
        self.project_name = "project_" + datetime.now().strftime("%Y%m%d_%H%M%S")
        self.full_path = os.path.join(self.root_folder, self.project_name)
        self.full_path_prompts = os.path.join(self.root_folder, self.project_name, "prompts")
        self.full_path_responses = os.path.join(self.root_folder, self.project_name, "responses")
        self.full_path_output = os.path.join(self.root_folder, self.project_name, "output")

    def get_key(self):
        return self.key
    
    def get_main_key(self):
        return self.main_key
    
    def get_sub_key(self):
        return self.sub_key

    def execute(self):
        self.create_project_directory()

    def create_project_directory(self):
        if not os.path.exists(self.full_path):
            os.makedirs(self.full_path)
            print(f"Created project directory: {self.full_path}")
        else:
            print(f"Project directory already exists: {self.full_path}")
                
        if not os.path.exists(self.full_path_prompts):
            os.makedirs(self.full_path_prompts)
            print(f"Created prompts directory: {self.full_path_prompts}")
        else:
            print(f"Prompts directory already exists: {self.full_path_prompts}")
            
        if not os.path.exists(self.full_path_responses):
            os.makedirs(self.full_path_responses)
            print(f"Created responses directory: {self.full_path_responses}")
        else:
            print(f"Responses directory already exists: {self.full_path_responses}")
            
        if not os.path.exists(self.full_path_output):
            os.makedirs(self.full_path_output)
            print(f"Created output directory: {self.full_path_output}")
        else:
            print(f"Output directory already exists: {self.full_path_output}")
            
        self.memory.create([self.main_key, self.key, self.sub_key], self.full_path)
        self.memory.create([self.main_key, self.key, "prompt_folder"], self.full_path_prompts)
        self.memory.create([self.main_key, self.key, "response_folder"], self.full_path_responses)
        self.memory.create([self.main_key, self.key, "output_folder"], self.full_path_output)

# modules/load_project.py

import os
import json
from ai import ModuleMemory, NLPProcessor

class LoadProject:
    def __init__(self, memory: ModuleMemory):
        self.main_key = "project"
        self.key = "initial_project_details"
        self.memory = memory
        
    def get_key(self):
        return self.key
    
    def get_main_subkey(self):
        return self.main_subkey
    
    def execute(self):
        # Get the current working directory
        current_directory = os.getcwd()

        # Filename you want to join with the current directory
        filename = "project.json"

        # Join the current directory with the filename
        project_file_path = os.path.join(current_directory, filename)
        
        print ("loading project:", project_file_path)

        self.load_project(project_file_path)
        # self.enhance_project()

    def load_project(self, project_file):
        """
        Load project details from a JSON file and store them in memory.
        """
        try:
            with open(project_file, 'r') as file:
                project_data = json.load(file)
                self.memory.create([self.main_key, self.key], project_data)
                print(f"Project '{project_data['name']}' loaded successfully.")
        except FileNotFoundError:
            print(f"Error: File '{project_file}' not found.")
        except json.JSONDecodeError:
            print("Error: JSON decoding error.")
        except Exception as e:
            print(f"An error occurred: {e}")


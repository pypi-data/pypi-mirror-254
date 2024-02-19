# test_app.py

import os
from maldinio_ai.tools.create_project_folder import CreateProjectFolder
from maldinio_ai.tools.load_project import LoadProject
from maldinio_ai.nlp.nlp_processor import NLPProcessor
from maldinio_ai.prompt.prompt_context import PromptContext
from maldinio_ai.prompt.prompt_generator import PromptGenerator
from maldinio_ai.prompt.response_processor import ResponseProcessor
from maldinio_ai.memory_management.memory_manager import ModuleMemory
from maldinio_ai.api.api_key_loader import OpenAIKeyLoader
from maldinio_ai.nlp.nlp_client import NLPClient

def main():
    # Load environment variables and API keys
    dotenv_path = os.path.join(os.getcwd(), ".env") # Ensure your .env file is in the current working directory
    key_loader = OpenAIKeyLoader(dotenv_path=dotenv_path)
    api_key = key_loader.get_api_key()

    # Initialize the memory module
    memory = ModuleMemory()
    
    # Create a new project folder
    create_folder = CreateProjectFolder(memory)
    create_folder.execute()
    
    # Load an existing project (Optional, demonstrate loading existing projects)
    # load_project = LoadProject(memory)
    # load_project.execute()
    
    # Set up NLP Client with API key
    nlp_client = NLPClient()  # Assume NLPClient is configured internally to use the API key
    
    # Initialize NLP Processor
    nlp_processor = NLPProcessor(memory=memory, nlp_client=nlp_client)
    
    # Define a prompt context
    prompt_context = PromptContext()
    prompt_context.update_context({
        'simple_prompt': 'Explain the concept of Artificial Intelligence.',
        'response_format': 'text'
    })
    
    # Generate a prompt based on the context
    prompt_generator = PromptGenerator(context=prompt_context)
    prompt = prompt_generator.generate_prompt()
    print(f"Generated Prompt:\n{prompt}")
    
    # Process the prompt with NLP
    processed_response = nlp_processor.process(prompt, prompt_context)
    print(f"Processed Response:\n{processed_response}")
    
    # Optionally, process the response to structure it (this part is customizable as needed)
    response_processor = ResponseProcessor(response_format='text')
    final_response = response_processor.process_response(processed_response)
    print(f"Final Response:\n{final_response}")

if __name__ == "__main__":
    main()
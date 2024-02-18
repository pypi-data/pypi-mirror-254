# from agents.project_items import FileList, File, FunctionalityList, Functionality, AIList
from .prompt_context import PromptContext

def convert_string(string):
    words = string.split('_')
    converted_words = [word.capitalize() for word in words]
    converted_string = ' '.join(converted_words)
    return converted_string


class PromptGenerator:
    def __init__(self, context: PromptContext = None, input_keys_data = None):
        if context is not None:
            self.set_context(context)
        self.input_keys_data = input_keys_data

    def set_context(self, context):
        self.promptcontext = context
        self.prefix = context.prefix or ""
        self.suffix = context.suffix or ""
        self.list_item = context.list_item or {}
        self.prompt = context.simple_prompt or ""
        self.context_items = context.context_items or []
        self.questions = context.questions or []
        self.examples = context.examples or []
        self.context = context.context or []
        self.instructions = context.instructions or []
        self.query = context.query or ""
        self.response_format = context.response_format or ""
        self.response_structure = context.response_structure or ""

    def generate_prompt(self):
        # Handle additional dynamic attributes
        known_attrs = ['role', 'prefix', 'suffix', 'list_item', 'simple_prompt', 'query', 'context_items', 'questions', 'examples',
                       'context', 'instructions', 'response_format', 'response_structure']
        # additional_attrs = [attr for attr in additional_attrs if not callable(getattr(self.context, attr))]
        additional_attrs = self.promptcontext.find_unknown_attributes(known_attrs)

        prompt = ""
        
        if self.prefix != "" and self.prefix is not None:
            prompt = f"{self.prefix}\n\n"
        
        prompt += f"## Prompt:\n{self.prompt}."
        
        if self.response_format != "" and self.response_format is not None:
            prompt += " " + f"Please provide your response in {self.response_format} format"
            prompt += " " + f"and in the requested structure which is shown below."
            prompt += "\n\n"
        else:
            prompt += "\n\n"
        

        if self.query != "" and self.query is not None:
            prompt += f"## Query:\n{self.query}\n\n"
        
        if self.list_item and self.list_item is not None:
            prompt += "## Current List Item:\n"
            for key, value in self.list_item.items():
                prompt += f"- {key}: {value}\n"
            prompt += "\n"

        if additional_attrs and additional_attrs is not None:
            prompt += "## Additional Context:\n"
            for attr in additional_attrs:
                value = getattr(self.promptcontext, attr)
                prompt += f"- {attr}: {value}\n"
            prompt += "\n"

        if self.context or self.context_items or self.input_keys_data is not None:
            prompt += "## Context:\n"
            
            if self.context and self.context is not None:
                for context_item in self.context:
                    prompt += f"- {context_item}\n"
                    
            if self.context_items and self.context_items is not None:
                for context_item in self.context_items.items():
                    key , context = context_item
                    # print()
                    # print ("checking key: ", key)
                    # print (context)
                    # print (type(context))
                    # print (isinstance(context, FileList))
                    # print (isinstance(context, FunctionalityList))
                    # print (isinstance(context, Functionality))
                    # print (isinstance(context, File))
                    # print (isinstance(context, str))
                    
                    ## if isinstance(context, FileList):
                    ##     file_list_prompt = context.generate_file_list_context()
                    ##     prompt += file_list_prompt + "\n"
                    ## elif isinstance(context, FunctionalityList):
                    ##     functionality_list_prompt = context.generate_functionality_context()
                    ##     prompt += functionality_list_prompt + "\n"
                    ## elif isinstance(context, AIList):
                    ##     ailist_prompt = context.generate_context()
                    ##     prompt += ailist_prompt + "\n"
                    ## else:
                    ##     key, context = context_item
                    ##     prompt += f"- {key}: {context}\n"
                    
                    prompt += f"- {key}: {context}\n"
            
            if self.input_keys_data:
                for key, value in self.input_keys_data.items():
                    prompt += f"- {key}: {value}\n"

            prompt += "\n"

        if self.instructions and self.instructions is not None:
            prompt += "## Instructions:\n"
            for idx, instruction in enumerate(self.instructions, start=1):
                prompt += f"{idx}. {instruction}\n"
            prompt += "\n"

        if self.questions and self.questions is not None:
            prompt += "## Questionaire:\n"
            for idx, question in enumerate(self.questions, start=1):
                prompt += f"{idx}. {question}\n"
            prompt += "\n"

        if self.examples and self.examples is not None:
            prompt += "## Examples:\n"
            for idx, example in enumerate(self.examples, start=1):
                prompt += f"{idx}. {example}\n"
            prompt += "\n"

        if self.response_format != "" and self.response_format is not None:
            prompt += "## Response Format:\n"
            prompt += f"Remember to provide your response in the format: {self.response_format}\n\n"

        if self.response_structure != "" and self.response_structure is not None:
            prompt += "## Expected Structure:\n"
            prompt += f"{self.response_structure}\n\n"

        prompt += f"{self.suffix}\n"
        
        return prompt



    def set_prompt_prefix(self, prefix = ""):
        
        if prefix == "":
            prompt_prefix = f"""## Project:\nPlease complete below instructions to complete the task. Provide your response in the given response format and in the expected structure.\n\n"""
        else:
            prompt_prefix = prefix

        self.prompt_prefix = prompt_prefix
        
        return prompt_prefix


    def set_prompt_instructions(self, instructions = None):
        
        prompt_text = ""
                
        if instructions is not None:
            prompt_text += f"\n\n## Instructions:\n"
            for instruction in instructions:
                prompt_text += "- " + instruction + "\n"

        self.prompt_body = prompt_text
        
        return prompt_text
    
    
    def set_prompt_body(self, prompt = "", prompt_body_items = None):
        prompt_text = ""
        
        if prompt != "":
            prompt_text = f"""## Task:\n{prompt}\n"""
        else:
            prompt_text = prompt
        
        if prompt_body_items is not None:
            for placeholder, replacement in prompt_body_items.items():
                
                placeholder_title = convert_string(placeholder)

                prompt_text += f"\n\n## {placeholder_title}:\n{{{{{placeholder}}}}}\n"
                placeholder = "{{" + placeholder + "}}"
                prompt_text = prompt_text.replace(placeholder, replacement)


        self.prompt_body = prompt_text
        
        return prompt_text

        

    def set_prompt_suffix(self, response_format = "json", expected_structure = "{ \"key\": \"value\"}"):

        prompt_suffix = f"\n## Response Format:\nRemember to provide your response in minified {response_format} format.In order to save tokens also avoid line breaks in the minified response. Do not add any further comments for automatic processing of the response.\n"

        if expected_structure and expected_structure != "{}":
            prompt_suffix += f"\n## Expected Structure:\n{expected_structure}\n"

        self.prompt_suffix = prompt_suffix
        
        return prompt_suffix
        
    def prepare_prompt_builder(self):
        self.set_prompt_prefix()
        self.set_prompt_body()
        self.set_prompt_suffix()
        self.set_prompt_instructions()
        self.use_prompt_builder = True
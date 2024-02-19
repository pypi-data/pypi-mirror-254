class PromptContext:
    def __init__(self, context_dict=None, **kwargs):
        if context_dict is None:
            context_dict = kwargs

        self.role = context_dict.get('role', '')
        self.prefix = context_dict.get('prefix', '')
        self.suffix = context_dict.get('suffix', '')
        self.list_item = context_dict.get('list_item', {})
        self.context_items = context_dict.get('context_items', {})
        self.context = context_dict.get('context', [])
        self.questions = context_dict.get('questions', [])
        self.examples = context_dict.get('examples', [])
        self.instructions = context_dict.get('instructions', [])
        self.query = context_dict.get('query', '')
        self.simple_prompt = context_dict.get('simplePrompt', '')
        self.response_format = context_dict.get('response_format', '')
        self.response_structure = context_dict.get('response_structure', '')

    def clean_context(self):
        """
        Reset all attributes of the instance.
        """
        for key in vars(self):
            setattr(self, key, None)

    def update_context(self, update_dict):
        """
        Update the context attributes based on the provided dictionary.
        Add new attributes if they do not exist.
        """
        self.clean_context()
        for key, value in update_dict.items():
            setattr(self, key, value)  # This will update or add a new attribute

    def add_attribute(self, key, value):
        """
        Add a new attribute to the instance.
        """
        setattr(self, key, value)
        
    def get_attribute(self, key):
        """
        Get the value of an attribute.
        """
        return getattr(self, key)

    def print_attributes(self):
        for key, value in self.__dict__.items():
            print(f"{key}: {value}")

    def find_unknown_attributes(self, known_attrs):
        """
        Returns a list of attribute names of the instance that are not in the known_attrs list.

        :return: A list of unknown attribute names.
        """
        preset_attrs = ['prefix', 'suffix', 'list_item', 'simple_prompt', 'query', 'context_items', 'questions', 'examples',
                       'context', 'instructions', 'response_format', 'response_structure'] if not known_attrs else known_attrs
        
        return [attr for attr in self.__dict__ if attr not in preset_attrs]

    def print_context(self):
        # Print all attributes of the instance
        for key in vars(self):
            value = getattr(self, key)
            if isinstance(value, dict):
                print(f"{key}:")
                for sub_key, sub_value in value.items():
                    print(f"- {sub_key}: {sub_value}")
            elif isinstance(value, list):
                print(f"{key}:")
                for item in value:
                    print(f"- {item}")
            else:
                print(f"{key}: {value}")

    def print_context(self):
        print("Role:", self.role)
        print("Prefix:", self.prefix)
        print("Suffix:", self.suffix)
        print("List Item:")
        for key, value in self.list_item.items():
            print(f"- {key}: {value}")
        print("Context Items:")
        for key, value in self.context_items.items():
            print(f"- {key}: {value}")
        print("Context:")
        for item in self.context:
            print(f"- {item}")
        print("Questionaire:")
        for question in self.questions:
            print(f"- {question}")
        print("Examples:")
        for example in self.examples:
            print(f"- {example}")            
        print("Instructions:")
        for instruction in self.instructions:
            print(f"- {instruction}")
        print("Query:", self.query)
        print("Simple Prompt:", self.simple_prompt)
        print("Response Format:", self.response_format)
        print("Response Structure:", self.response_structure)

import json

class ModuleMemory:
    def __init__(self):
        self.memory_store = {}

    def _navigate_to_node(self, path_list, create_missing=False):
        """
        Navigate to the node specified by the path list.
        If create_missing is True, missing nodes along the path will be created.
        """
        current_node = self.memory_store
        for key in path_list[:-1]:
            if key not in current_node:
                if create_missing:
                    current_node[key] = {}
                else:
                    raise KeyError(f"Path '{' > '.join(path_list)}' does not exist.")
            current_node = current_node[key]
        return current_node, path_list[-1]

    def save_response(self, response):
        """
        Save the response from OpenAI to memory.
        """
        self.memory_store['response'] = response
        
    def get_response(self):
        """
        Get the response from memory.
        """
        return self.memory_store.get('response')

    def create(self, path_list, value):
        """
        Create a new entry in memory at the specified path.
        """
        node, key = self._navigate_to_node(path_list, create_missing=True)
        if key in node:
            raise KeyError(f"Key '{key}' already exists at path '{' > '.join(path_list)}'.")
        node[key] = value

    def read(self, path_list):
        """
        Read an entry from memory at the specified path.
        """
        
        try:
            node, key = self._navigate_to_node(path_list)
        except KeyError:
            return None
        
        return node.get(key)

    def update(self, path_list, value):
        """
        Update an existing entry in memory at the specified path.
        """
        node, key = self._navigate_to_node(path_list)
        if key not in node:
            raise KeyError(f"Key '{key}' not found at path '{' > '.join(path_list)}'.")
        node[key] = value
        
    def create_or_update(self, path_list, value):
        """
        Create a new entry in memory at the specified path if it doesn't exist,
        otherwise update the existing entry.
        """
        node, key = self._navigate_to_node(path_list, create_missing=True)
        node[key] = value

    def delete(self, path_list):
        """
        Delete an entry from memory at the specified path.
        """
        node, key = self._navigate_to_node(path_list)
        if key in node:
            del node[key]


    def exists(self, key):
        """
        Check if a key exists in memory.
        """
        return key in self.memory_store

    def get_all_keys(self):
        """
        Get all keys in memory.
        """
        return list(self.memory_store.keys())

    def save_to_file(self, file_path):
        """Saves the current state of memory to a JSON file."""
        with open(file_path, 'w') as file:
            json.dump(self.memory_store, file, indent=4, sort_keys=True)

    def load_from_file(self, file_path):
        """Loads the current state of memory from a JSON file."""
        with open(file_path, 'r') as file:
            self.memory_store = json.load(file)
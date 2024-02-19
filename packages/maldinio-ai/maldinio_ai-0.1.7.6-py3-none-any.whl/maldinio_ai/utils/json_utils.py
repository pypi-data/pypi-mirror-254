import re
import json

def fix_json(json_data):
    try:
        # Attempt to directly parse the JSON first
        return json.loads(json_data)
    except json.JSONDecodeError:
        try:
            # Attempt to fix single quotes and re-parse
            fixed_json = json_data.replace("'", '"')
            return json.loads(fixed_json)
        except json.JSONDecodeError:
            # Handle other JSON errors
            return None

def verify_json(json_data, structure):
    
    debug = False

    if debug == True:
        print ("json_data: ", json_data)
        print ("structure: ", structure)
        print ("--------------------------------")
        print ()
        
        data = json.loads(json_data)

        comparison_result = compare_structure(data, structure)

    data = fix_json(json_data)
    if data is not None:
        comparison_result = compare_structure(data, structure)
        return comparison_result
    else:
        # Handle other JSON errors
        return False
        
def compare_structure(data, structure):
    if isinstance(structure, type):
        return isinstance(data, structure)

    if isinstance(structure, dict):
        for key, value_structure in structure.items():
            if key not in data or not compare_structure(data[key], value_structure):
                return False

    elif isinstance(structure, list):
        # Handling list of primitives separately
        if isinstance(structure[0], type):
            return all(isinstance(item, structure[0]) for item in data)
        else:
            if not all(isinstance(item, type(structure[0])) for item in data):
                return False
            for item in data:
                if not compare_structure(item, structure[0]):
                    return False

    return True



def generate_string_from_json(json_obj):
    def process_value(value):
        if isinstance(value, dict):
            return generate_string_from_json(value)
        elif isinstance(value, list):
            if value:
                element = process_value(value[0])
                return f"[{element}]"
            else:
                return "[]"
        else:
            return str(value)


    string_representation = "{"
    for key, value in json_obj.items():
        processed_value = process_value(value)
        string_representation += f'"{key}": {processed_value}, '
    string_representation = string_representation.rstrip(", ")
    string_representation += "}"
    return string_representation

# Example usage
expected_structure = {
    "nlp_task": str,
    "task_description": str,
    "nested_array": [str],
    "nested_object": {
        "property1": int,
        "property2": float
    }
}




def convert_json_to_python_object(json_dict):
    # Define a dictionary to store the converted Python object structure
    python_object = {}

    # Define a mapping from type string to Python type
    types_mapping = {
        "str": str,
        "int": int,
        "float": float,
        "bool": bool,
        "null": type(None),
        "list": list,
        "tuple": tuple,
        "dict": dict,
        "set": set,
        "frozenset": frozenset,
        "complex": complex,
        "bytes": bytes,
        "bytearray": bytearray
    }

    # Iterate over each key-value pair in the JSON dictionary
    for key, value in json_dict.items():
        # If the value is a list, recursively call this function for each element
        if isinstance(value, list):
            python_object[key] = [convert_json_to_python_object(v) if isinstance(v, dict) else types_mapping.get(v, v) for v in value]
        # If the value is a nested dictionary, recursively call this function
        elif isinstance(value, dict):
            python_object[key] = convert_json_to_python_object(value)
        # If the value is a type string, convert it to the corresponding Python type
        else:
            python_object[key] = types_mapping.get(value, value)

    return python_object



# Example usage:
obj = {
    "step_number": int,
    "step_description": str,
    "name": str,
    "description": str,
    "tasks": [
        {
            "task_name": str,
            "task_type": str,
            "tree_of_thought": bool,
            "quality_check": bool,
            "input_values": [str],
            "output_values": [str],
            "prompt": str,
            "expected_structure": {
                "functionalities": [str]
            },
            "replacements": dict
        }
    ]
}


def generate_expected_structure_string(expected_structure):
    expected_structure_object = convert_json_to_python_object(expected_structure)
    expected_structure_object_string = generate_string_from_json(expected_structure)
    return expected_structure_object_string



def convert_python_object_to_json(obj):
    # Helper function to convert Python types to serializable types
    def convert_type(value):
        if isinstance(value, type):
            return value.__name__
        return value

    # Recursively convert the object to JSON-compatible types
    def convert(obj):
        if isinstance(obj, dict):
            return {key: convert(value) for key, value in obj.items()}
        elif isinstance(obj, list):
            return [convert(value) for value in obj]
        else:
            return convert_type(obj)

    # Convert the object to JSON representation
    json_representation = json.dumps(convert(obj), indent=4)
    return json_representation


def extract_json_from_message(message):
    start_token = "{"
    end_token = "}"

    # Find the start and end indices of the JSON object within the message
    start_index = message.find(start_token)
    end_index = message.rfind(end_token)

    if start_index == -1 or end_index == -1:
        return "JSON object not found in the message"

    # Extract the JSON object from the message
    json_string = message[start_index:end_index + len(end_token)]

    # Parse the JSON string into a Python object
    json_data = json.loads(json_string)

    return json_data


def extract_json_string_from_message(message):
    start_token = "{"
    end_token = "}"

    # Find the start and end indices of the JSON object within the message
    start_index = message.find(start_token)
    end_index = message.rfind(end_token)

    if start_index == -1 or end_index == -1:
        return "JSON object not found in the message"

    # Extract the JSON object from the message
    json_string = message[start_index:end_index + len(end_token)]

    return json_string


def cleanup_json_response(response):
    
    if response.startswith("```json"):
        # Use regular expressions to extract the entire JSON block
        json_pattern = r'```json\s*(\{.*?\})\s*```'
        match = re.search(json_pattern, response, re.DOTALL)
        
        if match:
            json_block = match.group(1)
            try:
                # Parse the JSON string
                json_data = json.loads(json_block)
                return json_block

            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
                # Attempt to fix by adding a closing bracket
                fixed_json_block = json_block + "}"
                try:
                    # Parse the fixed JSON string
                    json_data = json.loads(fixed_json_block)
                    return fixed_json_block
                except json.JSONDecodeError:
                    print("Failed to fix JSON.")
        else:
            print("JSON data not found in the input string.")

    return response
import json
from utils.json_utils import extract_json_from_message, extract_json_string_from_message


def validate_json_structure_noarray(json_data, expected_structure):
    for key, value_type in expected_structure.items():
        print (key, value_type)
        if key not in json_data or not isinstance(json_data[key], value_type):
            return False
    return True

def validate_json_structure(json_data, expected_structure):
    for key, value_type in expected_structure.items():
        print ('key, value_type', key, value_type)
        
        
        if key not in json_data:
            print ('key not in json_data')
            
            return False
        if isinstance(value_type, list):
            print ('value_type is list')
            if not isinstance(json_data[key], list):
                print ('json_data[key] is not list')
                return False
            # Validate each item in the array
            for item in json_data[key]:
                print ('item', item)
                if not isinstance(item, value_type[0]):
                    print ('item is not value_type[0]')
                    return False
        else:
            print ('value_type is not list')
            if not isinstance(json_data[key], value_type):
                print ('json_data[key] is not value_type')
                return False
    return True


def validate_data(data):
    # Add your specific validation logic here
    return True

def validate_subtasks(subtasks):
    for subtask in subtasks:
        if not isinstance(subtask, dict):
            return False
        expected_keys = ["id", "name", "description", "status"]
        for key in expected_keys:
            if key not in subtask or not isinstance(subtask[key], str):
                return False
    return True
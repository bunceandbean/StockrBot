import sys
import json

# This function reads a python dict and saves it as a .json file in Saves
def save_to_json(py_dict, name, dirs=""):
    if type(py_dict) != type({}) or type(name) != type(""):
        print("Error: Object was not a 'dict' or name was not a 'string'.")
        sys.exit()
    with open(dirs + name + ".json", 'w') as f:
        json.dump(py_dict, f)

# This function loads in a .json file from Saves and returns a dictionary
def load_from_json(name, dirs=''):
    if type(name) != type(""):
        print("Error: Object was not a 'dict' or name was not a 'string'.")
        sys.exit()
    with open(dirs + name + ".json", 'r') as f:
        return json.load(f)

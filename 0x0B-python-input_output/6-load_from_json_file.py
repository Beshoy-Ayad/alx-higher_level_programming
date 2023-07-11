#!/usr/bin/python3
"""module to create an object from a JSON file"""

import json  # Import the json module


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”"""
    # Use the with statement to open the file in read mode
    with open(filename, "r", encoding="utf-8") as f:
        # Use the json.load() function to create an
        # object from the file using JSON
        return json.load(f)

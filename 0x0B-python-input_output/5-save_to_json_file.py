#!/usr/bin/python3
"""module to write an object to a text file using JSON"""

import json  # Import the json module


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation"""
    # Use the with statement to open the file in write mode
    with open(filename, "w", encoding="utf-8") as f:
        # Use the json.dump() function to write the object
        # to the file using JSON
        json.dump(my_obj, f)

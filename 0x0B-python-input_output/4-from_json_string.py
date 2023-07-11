#!/usr/bin/python3
"""module to convert a JSON string to an object"""

import json  # Import the json module


def from_json_string(my_str):
    """Returns an object (Python data structure)
    represented by a JSON string"""
    # Use the json.loads() function to convert the JSON string to an object
    return json.loads(my_str)

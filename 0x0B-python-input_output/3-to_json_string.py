#!/usr/bin/python3
"""module to convert an object to a JSON string"""


import json  # Import the json module


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)"""
    # Use the json.dumps() function to convert the object to a JSON string
    return json.dumps(my_obj)

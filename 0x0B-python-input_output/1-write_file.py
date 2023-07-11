#!/usr/bin/python3
"""module to write a string to a text file"""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns the number of
    characters written"""
    # Use the with statement to open the file in write mode
    with open(filename, "w", encoding="utf-8") as f:
        # Write the text to the file and return the number of
        # characters written
        return f.write(text)

#!/usr/bin/python3
"""module to append a string to a text file"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file and
    returns the number of characters added"""
    # Use the with statement to open the file in append mode
    with open(filename, "a", encoding="utf-8") as f:
        # Write the text to the file and return the number of
        # characters written
        return f.write(text)

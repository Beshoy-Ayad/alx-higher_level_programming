#!/usr/bin/python3
""" Python 3.8.5"""


def lookup(obj):
    """
    A function that takes an object as input and returns a list of all the attributes and methods of that object.

    Parameters:
    - obj: An object that will be used to look up the attributes and methods.

    Returns:
    - A list of strings representing the attributes and methods of the input object.
    """
    """"""
    return (dir(obj))

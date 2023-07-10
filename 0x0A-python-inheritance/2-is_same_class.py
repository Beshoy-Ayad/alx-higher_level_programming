#!/usr/bin/python3
"""returns True if the object is exactly an instance
of the specified class ; otherwise False"""


def is_same_class(obj, a_class):
    """
    Determines if an object is an instance
    of a specified class.

    Parameters:
        obj (Any): The object to check the class of.
        a_class (type): The class to compare against.

    Returns:
        bool: True if the object is an instance
        of the specified class, False otherwise.
    """

    x = type(obj)
    if x == a_class:
        return True
    return False

#!/usr/bin/python3
"""
    Print the sorted elements of the calling object.
"""


class MyList(list):
    """
        Parameters:
            self (list): The list to be sorted and printed.
    """

    def print_sorted(self):
        """
        Returns:
            None
        """
        print(sorted(self))

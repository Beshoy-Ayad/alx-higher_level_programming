#!/usr/bin/python3
""" Definition of a class to represent a rectangle
"""


class Rectangle():
    """ Represent a rectangle
    """
    def __init__(self, width=0, height=0):
        """ Instantiate a rectangle
        """
        self.height = height
        self.width = width

    def __del__(self):
        print("Bye rectangle...")

    def __str__(self):
        if self.height and self.width:
            return '\n'.join(['#' * self.width] * self.height)
        return ''

    def __repr__(self):
        return 'Rectangle({}, {})'.format(self.width, self.height)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width and self.height:
            return 2 * (self.width + self.height)
        return 0

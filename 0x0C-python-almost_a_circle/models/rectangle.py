#!/usr/bin/python3

from models.base import Base

class Rectangle(Base):
    """A class that represents a rectangle"""

    # private instance attributes, each with its own public getter and setter
    __width = 0
    __height = 0
    __x = 0
    __y = 0

    # class constructor
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle instance"""
        # call the super class with id
        super().__init__(id)
        # assign each argument to the right attribute
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # public getter for width
    @property
    def width(self):
        """Return the width of the rectangle"""
        return self.__width

    # public setter for width
    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        # validate the value
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        # assign the value to the private attribute
        self.__width = value

    # public getter for height
    @property
    def height(self):
        """Return the height of the rectangle"""
        return self.__height

    # public setter for height
    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        # validate the value
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        # assign the value to the private attribute
        self.__height = value

    # public getter for x
    @property
    def x(self):
        """Return the x coordinate of the rectangle"""
        return self.__x

    # public setter for x
    @x.setter
    def x(self, value):
        """Set the x coordinate of the rectangle"""
        # validate the value
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        # assign the value to the private attribute
        self.__x = value

    # public getter for y
    @property
    def y(self):
        """Return the y coordinate of the rectangle"""
        return self.__y

    # public setter for y
    @y.setter
    def y(self, value):
        """Set the y coordinate of the rectangle"""
        # validate the value
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        # assign the value to the private attribute
        self.__y = value

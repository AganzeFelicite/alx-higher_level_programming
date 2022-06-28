#!/usr/bin/python3
"""
    this is a rectangle modules
"""


class Rectangle:
    """
        this is a rectangle class
        Args:
            width(int)
            height(int)
        methodes
            setters and getters
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
            return a private width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ pass in a on a positive int"""
        if type(value) is not int:
            raise TypeError("width must  be an integer")
        elif value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ this is  property to retrieve the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """ this is a height setter provately within the class"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise TypeError("height must be >= 0")
        
        self.__height = value

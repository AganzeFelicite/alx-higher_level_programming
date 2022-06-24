#!/usr/bin/python3
""" a class that defines a square"""


class Square:
    """Defines methods for the class Square"""
    def __init__(self, size=0):
        """check the conditions"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        """this is an instantion in square"""
        self.__size = size
    """to calculate the area of the class"""
    def area(self):
        return self.__size * self.__size
    """this is a size getter"""
    @property
    def size(self):
        return self.__size
    """this is a size setter"""
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    """this is to print the square object"""
    def my_print(self):
        """print the square"""
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
        if self.__size = 0:
            print("")

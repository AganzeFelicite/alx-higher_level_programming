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

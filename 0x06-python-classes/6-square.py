#!/usr/bin/python3
"""definition of the class square"""


class Square:
    """an instantiation"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """self is the current object"""
        return self.__size
        """this is a setter for the size init attrubute"""
    @size.setter
    def size(self, value):
        """value is the size to be entered it should be an int"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value == 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """return the position tuple"""
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integer")
        elif value[0] is not int or value[0] < 0:
            raise TypeError("position must be a tuple of 2 positive integer")
        elif type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integer")
        else:
            self.__position = value     # only with 2 ints in the tuple

    @property
    def area(self):
        return self.__size ** 2

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

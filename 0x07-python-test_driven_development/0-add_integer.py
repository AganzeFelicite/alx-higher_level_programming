#!/usr/bin/python3
""" 0-add_module 
    to add 
    two ints

"""


def add_integer(a, b=0):
    """Return the addition of two numbers"""
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        numa, numb = int(a), int(b)
        return numa + numb

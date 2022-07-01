#!/usr/bin/python3
""" 0-add_module"""


def add_integer(a, b=98):
    """"
    this add two integers
    Args:
        a(int)
        b(int)
    the arguments must be passed in
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        numa, numb = int(a), int(b)
        return numa + numb

#!/usr/bin/python3
"""this print only integers and raise exceptions when its not"""


def safe_print_integer(value):
    """returns true when its an int and false for a string"""
    try:
        print("{:d}".format(value))
        return True
    except ValueError as err:
        return False

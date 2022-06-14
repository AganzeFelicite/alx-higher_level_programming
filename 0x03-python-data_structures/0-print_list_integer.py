#!/usr/bin/python3
def print_list_integer(my_list=[]):
    """
    prints all integers in a list

    Args:
        my_list: list of integers
    """

    for integer in my_list:
        print("{:d}".format(integer))

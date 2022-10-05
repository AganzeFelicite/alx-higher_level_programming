#!/usr/bin/python3
"""prints the first elements of a string only integers"""


def safe_print_list_integers(my_list=[], x=0):
    """print all integers of the list on the same line"""
    realnum = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            realnum += 1
        except (ValueError, TypeError):
            pass
    print()
    return realnum

#!/usr/bin/python3
"""this print elements of a lists in anorder"""


def safe_print_list(my_list=[], x=0):
    '''this prints the list elements'''
    try:
        for i in range(x):
            print(my_list[i], end="")
        print()
    except IndexError:
        print()
    finally:
        return i + 1

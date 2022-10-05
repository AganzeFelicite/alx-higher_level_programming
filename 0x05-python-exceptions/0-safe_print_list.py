#!/usr/bin/python3
"""this print elements of a lists in anorder"""

def safe_print_list(my_list=[], x=0):
    '''this prints the list elements'''
    val = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            val += 1
        print()
        return val
    except IndexError:
        print()
        return val

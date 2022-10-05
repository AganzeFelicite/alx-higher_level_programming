#!/usr/bin/python3
"""this print elements of a lists in anorder"""


from http.client import CannotSendRequest


def safe_print_list(my_list=[], x=0):
    '''this prints the list elements'''
    counting = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            counting += 1
        print()
        return counting
    except IndexError:
        print()
        return counting

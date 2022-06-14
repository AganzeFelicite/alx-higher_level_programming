#!/usr/bin/python3
def no_c(my_string):
    """
    Removes all characters c and C from a string

    Args:
        my_string: string to remove characters from

    Return:
        new string
    """
    return my_string.translate({ord('c'): None, ord("C"): None})

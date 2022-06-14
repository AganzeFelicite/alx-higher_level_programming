#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    Finds the biggest integer of a list

    Args:
        my_list: list to check from

    Return:
        biggest integer of list or none if
        list is empty
    """
    if not my_list:
        return None

    highest = my_list[0]
    for integer in my_list:
        highest = integer if (integer > highest) else highest
    return highest

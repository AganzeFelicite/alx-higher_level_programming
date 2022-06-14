#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    Finds all multiples of 2 in the list

    Args:
        my_list: list to check from

    Return:
        list of true or false, if a number is
        a multiple of 2 or not
    """
    new_list = []
    for integers in my_list:
        if integers % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list

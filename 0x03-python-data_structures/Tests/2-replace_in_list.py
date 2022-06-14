#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    Replaces an element at a specific position

    Args:
        my_list: list containing element to be changed
        idx: index to change element
        element: element to replace pre-existing element

    Return:
        new list if index was reached or old list if not
    """
    if idx < 0:
        return my_list
    if idx >= len(my_list):
        return my_list

    for index in range(len(my_list)):
        if index == idx:
            my_list[index] = element
            return my_list

#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    Replaces an element in a list at a specific position
    without modifying the original list

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

    new_list = []
    for index, item in enumerate(my_list):
        if index == idx:
            new_list.append(element)
            continue
        new_list.append(item)
    return new_list

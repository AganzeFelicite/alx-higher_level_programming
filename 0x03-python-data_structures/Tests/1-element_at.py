#!/usr/bin/python3
def element_at(my_list, idx):
    """
    Retrieves an element from a list

    Args:
        my_list: list to retreive element from
        idx: index to retrieve element

    Return:
        element at index or None if not found
    """
    if idx < 0:
        return None
    if idx >= len(my_list):
        return None

    for index, element in enumerate(my_list):
        if index == idx:
            return element

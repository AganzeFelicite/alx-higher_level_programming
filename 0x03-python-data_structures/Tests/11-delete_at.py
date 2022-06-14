#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    Deletes the item at a specific position in a list

    Args:
        my_list: list to make changes on
        idx: index to delete from

    Return:
        new deleted list or none if index is not
        accessible
    """
    if idx < 0 or idx >= len(my_list):
        return my_list

    del my_list[idx]
    return my_list

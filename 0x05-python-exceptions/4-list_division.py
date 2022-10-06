#!/usr/bin/python3
"""This devides the elements of two array"""


def list_division(my_list_1, my_list_2, list_length):
    """this return a list of the divided values"""
    new_list = []
    try:
        for i in range(list_length):
            try:
                result = my_list_1[i] / my_list_2[i]
                new_list.append(result)
            except(TypeError, ValueError):
                print("wrong type")
                new_list.append(0)
            except ZeroDivisionError:
                print("division by 0")
                new_list.append(0)
            except IndexError:
                print("out of range")
                new_list.append(0)
    finally:
        return new_list

#!/usr/bin/python3
''' this is the is_same_class module'''


def is_same_class(obj, a_class):
    ''' this is a function to check if a give object is in a class'''
    if type(obj) is not a_class:
        return False
    else:
        return True

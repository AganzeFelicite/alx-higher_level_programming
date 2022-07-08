#!/usr/bin/python3
""" this is the inherits_from module"""


def inherits_from(obj, a_class):
    """ this returns true if the object is an instance of a class"""
    if type(obj) is not a_class:
        if isinstance(obj, a_class):
            return True
    return False

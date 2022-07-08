#!/usr/bin/python3
'''look up module'''


def lookup(obj):
    '''
        this is a function to return all attributes and methods in an object
        Args:
            it receive an object and returns an array of the above mentioned

    '''
    return dir(obj)

#!/usr/bin/python3
'''this is MyList Module'''


class MyList(list):
    ''' this is my class'''
    def print_sorted(self):
        """ this should sort the  array object"""
        print(sorted(self))

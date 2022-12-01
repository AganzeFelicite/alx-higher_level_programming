#!/usr/bin/python3
"""a class"""


class Student:
    """a class """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list:
            dict = {}
            for i in attrs:
                item = self.__dict__.get(i)
                if item is not None:
                    dict[i] = item
            return dict
        return self.__dict__

    def reload_from_json(self, json):
        dicts = self.__dict__
        for key, val in json.items():
            if key in dicts.keys():
                self.__dict__[key] = val

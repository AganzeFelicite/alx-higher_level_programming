#!/usr/bin/python3
""" this is the base class module"""


class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        """
        this is the init function of the class/constructor
        Args:
        """
        if id is not None:
            self.id = int(id)
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

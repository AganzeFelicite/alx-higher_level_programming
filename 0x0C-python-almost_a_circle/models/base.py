#!/usr/bin/python3
""" this is the base class """


class Base:
    """ this is the classs with its class private
    variable
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ this is the class constructor of the base class
        """

        if id is not None:
            '''when id is provided'''

            self.id = id
        else:
            ''' when the id is not provided'''

            Base.__nb_objects += 1
            self.id = Base.__nb_objects

#!/usr/bin/python3
"""this to convert a json string to a python object"""

import json


def from_json_string(my_str):
    """into python obj"""

    py_obj = json.loads(my_str)
    return py_obj

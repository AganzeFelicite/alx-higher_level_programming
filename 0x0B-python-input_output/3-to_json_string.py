#!/usr/bin/python3
"""serialise into python obj"""


import json


def to_json_string(my_obj):
    """serialize"""
    obj = json.dumps(my_obj)
    return obj

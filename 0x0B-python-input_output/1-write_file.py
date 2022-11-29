#!/usr/bin/python3
"""this is to return number of char writen"""


def write_file(filename="", text=""):
    """write_to_file in python"""
    if type(filename) is str:
        with open(filename, mode="w", encoding="utf-8") as f:
            return f.write(text)

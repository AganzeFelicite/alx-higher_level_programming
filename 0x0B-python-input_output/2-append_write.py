#!/usr/bin/python3
"""learn to append to the end of a file in python"""


def append_write(filename="", text=""):
    """at the end and return the number of chars"""
    if type(filename) is str:
        with open(filename, mode="a", encoding="utf-8") as f:
            return f.write(text)

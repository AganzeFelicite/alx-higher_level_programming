#!/usr/bin/python3
"""this is to create a file in python"""


def read_file(filename=""):
    """use the with statement"""

    if type(filename) is str:
        with open(filename, mode="r", encoding="utf-8") as f:
            print(f.read())

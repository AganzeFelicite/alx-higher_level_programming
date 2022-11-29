#!/usr/bin/python3
"""this is to create a file in python"""


def read_file(filename=""):
    with open(filename, encoding="utf-8") as f:
        a = f.read()
        print(a)

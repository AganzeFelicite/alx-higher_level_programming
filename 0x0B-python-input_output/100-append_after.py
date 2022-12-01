#!/usr/bin/python3
""" Search for a word in a string and append there a string"""


def append_after(filename="", search_string="", new_string=""):
    """should append after searching into the string"""

    with open(filename, mode="r", encoding="utf-8") as f:
        lines = f.readlines()
        content = []
        for line in lines:
            content.append(line)
            if search_string in line:
                content.append(new_string)

    with open(filename, mode="w", encoding="utf-8") as f:
        new = "".join(content)
        f.write(new)

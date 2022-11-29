#!/usr/bin/python3
"""into a file using a JSON representation"""

import json


def save_to_json_file(my_obj, filename):
    """convert an object into a json txtfile"""

    with open(filename, mode="w", encoding="utf-8") as f:
        return json.dump(my_obj, f)

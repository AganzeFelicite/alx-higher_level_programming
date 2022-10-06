#!/usr/bin/python3
"""divides the integers and prints the results"""


def safe_print_division(a, b):
    result = 0
    try:
        result = a / b
        print("Inside result: {}".format(result))
        return result
    except (ZeroDivisionError):
        result = None
        print("Inside result: {}".format(result))
    finally:
        return result

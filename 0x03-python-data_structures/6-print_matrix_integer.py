#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers.

    Args:
        matrix: a 2D list
    """

    for array in matrix:
        space = ""
        for item in array:
            print("{}{:d}".format(space, item), end="")
            space = " "
        print()

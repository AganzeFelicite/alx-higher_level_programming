#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    number_of_args = len(argv) - 1

    if number_of_args == 0:
        print("{} arguments.".format(number_of_args))
    elif number_of_args == 1:
        print("{} argument:".format(number_of_args))
        print("{}: {}".format(number_of_args, argv[1]))
    else:
        print("{} arguments:".format(number_of_args))
        comb = [f"{i}: {lin}"for i, lin in enumerate(argv) if lin != argv[0]]
        print("\n".join(comb))

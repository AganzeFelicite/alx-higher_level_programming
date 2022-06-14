#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    argument_length = len(argv) - 1
    if argument_length == 0:
        print(0)
    else:
        addition = sum(map(int, [word for word in argv if word != argv[0]]))
        print(addition)

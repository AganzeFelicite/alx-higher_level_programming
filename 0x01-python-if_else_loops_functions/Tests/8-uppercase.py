#!/usr/bin/python3
def uppercase(str):
    for char in str:
        asc = ord(char)
        compute = asc - 32 if (97 <= asc <= 122) else asc
        print("{:c}".format(compute), end="")
    print()

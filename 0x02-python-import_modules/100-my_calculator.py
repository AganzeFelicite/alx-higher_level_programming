#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div

    number_of_args = len(argv) - 1

    if number_of_args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])

    operators = ["+", "-", "/", "*"]
    functions = [add(a, b), sub(a, b), div(a, b), mul(a, b)]
    if not (argv[2] in operators):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    for operate, func in zip(operators, functions):
        if operate == argv[2]:
            break

    print("{:d} {} {:d} = {:d}".format(a, argv[2], b, func))

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = -(abs(number) % 10) if (number < 0) else number % 10
sting = f"Last digit of {number:d} is {lastdigit}"
if lastdigit > 5:
    print(f"{sting} and is greater than 5")
elif lastdigit == 0:
    print(f"{sting} and is 0")
else:
    print(f"{sting} less than 6 and not 0")

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last_dig = -(abs(number) % 10) if (number < 0) else number % 10
start = f"Last digit of {number:d} is {last_dig}"
if last_dig > 5:
    print(f"{start} and is greater than 5")
elif last_dig == 0:
    print(f"{start} and is 0")
else:
    print(f"{start} and is less than 6 and not 0")

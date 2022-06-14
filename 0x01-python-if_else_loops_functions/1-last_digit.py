#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = -(abs(number) % 10) if number < 0 else int(repr(number)[-1])
print("Last digit of {} is {} ".format(number, lastdigit), end=" ")
if lastdigit > 5:
    print("and is greater than 5")
elif lastdigit == 0:
    print("and is 0")
else:
    print("less than 6 and not 0")

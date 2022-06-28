#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a = "Last digit of "
if number < 0:
    l = ((number * -1) % 10) * -1
else:
    l = number % 10
    if l > 5:
        print("{}{} is {} and is greater than 5".format(a, number, l))
    elif l == 0:
        print("{}{} is {} and is 0".format(a, number, l))
    elif l < 6 and l != 0:
        print("{}{} is {} and is less than 6 and not 0".format(a, number, l))

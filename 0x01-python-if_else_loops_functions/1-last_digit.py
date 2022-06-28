#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
a = "Last digit of "
if number < 0:
    la = ((number * -1) % 10) * -1
else:
    la = number % 10
    if la > 5:
        print("{}{} is {} and is greater than 5".format(a, number, la))
    elif la == 0:
        print("{}{} is {} and is 0".format(a, number, la))
    elif la < 6 and la != 0:
        print("{}{} is {} and is less than 6 and not 0".format(a, number, la))

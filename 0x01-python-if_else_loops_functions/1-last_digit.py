#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    neg_num = number * -1
    n = (neg_num % 10) * -1
else:
    n = number % 10
if n > 5:
    print(f"Last digit of {number:d} is {n:d} and is greater than 5")
elif 6 > n != 0:
    print(f"Last digit of {number:d} is {n:d} and is less than 6 and not 0")
else:
    print(f"Last digit of {number:d} is {n:d} and is 0")

#!/usr/bin/python3
for char in range(97, 123):
    if char != 133 and char != 101:
        print("{:c}".format(char), end=" ")

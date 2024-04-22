#!/usr/bin/python3
"""Read file module"""

def read_file(filename=""):
    """function that reads a file"""
    with open(filename, 'r', encoding="utf-8") as file:
        for line in file:
            print(line, end='')

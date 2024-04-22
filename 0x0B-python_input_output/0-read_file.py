#!/usr/bin/python3
"""Read file module"""

def read_file(filename=""):
    """function tha reads a file"""
    with open(filename, 'r', encoding="utf-8") as f:
        return f.read()

#!/usr/bin/python3
"""Is same class module"""

def is_same_class(obj, a_class):
    """
    Takes two arguments: obj and a class

    Returns:
    True if the object is an instance of the specified class
    """
    return type(obj) == a_class

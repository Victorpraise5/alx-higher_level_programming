#!/usr/bin/python3
"""Only sub class of"""

def inherits_from(obj, a_class):
    """
    Takes two arguments:
    obj and a class

    Returns:
    True if the object is an instance of a class that inherited
    """
    return isinstance(obj, a_class) and type(obj) != a_class

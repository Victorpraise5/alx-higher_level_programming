#!/usr/bin/python3
"""Lookup Module"""

def lookup(obj):
    """
    Get the list of available attributes and methods of an object.

    Args:
    obj: Any object

    Returns:
    List of available attributes and methods
    """
    return dir(obj)

#!/usr/bin/python3
"""
This module contains the base class for the project
"""

class Base:
    """
    This class will be the Base of all other classes in this project
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of data """
        if id != None:
            self.id = id
        else:
            __nb_objects += 1
            id = __nb_objects

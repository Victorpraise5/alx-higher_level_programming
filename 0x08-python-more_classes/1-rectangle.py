#!/usr/bin/python3
"""Rectangle module"""

class Rectangle:
    """rectangle class"""

    def __init__(self, width=0, height=0):
        """Initializing data"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """to retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """to set the width"""
        if isinstance(value, int):
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >=0")
        else:
            raise TypeError("width must be an integer")

    @property
    def height(self):
        """to retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """to set the height"""
        if isinstance(value, int):
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >=0")
        else:
            raise TypeError("height must be an integer")

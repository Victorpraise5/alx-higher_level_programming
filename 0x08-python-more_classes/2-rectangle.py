#!/usr/bin/python3
"""rectangle module"""

class Rectangle:
    """rectangle class"""

    def __init__(self, width=0, height=0):
        """initializing data"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """to retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """to set width"""
        if isinstance(value, int):
            if value >=0:
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
        """to set height"""
        if isinstance(value, int):
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height mus be >=0")
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__width == 0 and self.__height == 0:
            perimeter = 0
        else:
            perimeter = (self.__width + self.__height) * 2
        return perimeter

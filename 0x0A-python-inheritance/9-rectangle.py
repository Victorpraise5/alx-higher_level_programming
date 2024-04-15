#!/usr/bin/python3
"""Rectangle module"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """initialize Rectangle"""
        self.__width = width
        self.integer_validator("width", width)
        self.__height = height
        self.integer_validator("height", height)

    def area(self):
        """to implement the area"""
        return self.__width * self.__height

    def __str__(self):
        """return string representation of the rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"

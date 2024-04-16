#!/usr/bin/python3
"""square module"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """square class"""

    def __init__(self, size):
        """initializing data"""
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """implements the area"""
        return self.__size ** 2

    def __str__(self):
        """returns the square description"""
        return f"[Square] {self.__size} / {self.__size}"

#!/usr/bin/python3
"""square module"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """initializing data"""
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """to implement the area"""
        return self.__size ** 2

    def __str__(self):
        """string representation of the sqaure"""
        return f"[Square] {self.__size}/{self.__size}"

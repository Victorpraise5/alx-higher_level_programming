#!/usr/bin/python3
"""rectangle module"""

class Rectangle:
    """rectangle class"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initializing data"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """to retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """to set width"""
        if isinstance(value, int):
            if value >= 0:
                self.__width = value
            else:
                raise ValueError("width must be >=0")
        else:
            raise TypeError("width mus be an integer")

    @property
    def height(self):
        """to retrieve the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """to set the height"""
        if isinstance(value, int):
            if value >= 0:
                self.__height = value
            else:
                raise ValueError("height must be >= 0")
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__width == 0 and self.__height == 0:
            perimeter = 0
        else:
            perimeter = (self.__width + self.__height) * 2
        return perimeter

    def __str__(self):
        """to print the rectangle in #"""
        result = ""
        if self.__width == 0 or self.__height == 0:
            return result
        else:
            for i in range(self.__height):
                result += "#" * self.__width + "\n"
            return result.strip()

    def __repr__(self):
        """returns a string representation of the rectangle"""
        return f'Rectangle({self.__width}, {self.__height})'
    def __del__(self):
        """to delete"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

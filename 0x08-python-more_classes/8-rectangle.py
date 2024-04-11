#!/usr/bin/python3
"""rectangle module"""

class Rectangle:
    """rectangle class"""
    number_of_instance = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """initializing data"""
        self.width = width
        self.height = height
        Rectangle.number_of_instance += 1

    @property
    def width(self):
        """to retrieve the width"""
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
        """to retrieve the height"""
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
        """print the rectangle with #"""
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
        """deletes"""
        print("Bye rectangle...")
        Rectangle.number_of_instance -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("retc_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_rect_1 = rect_1.area()
        area_rect_2 = rect_2.area()

        if area_rect_1 >=  area_rect_2:
            return rect_1
        else:
            return rect_2

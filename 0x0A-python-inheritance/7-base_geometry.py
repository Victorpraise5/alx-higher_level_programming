#!/usr/bin/python3
"""BaseGeometry module"""

class BaseGeometry():
    """BaseGeometry class"""

    def area(self):
        """Raises an Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates Value"""
        if isinstance(value, int):
            if value >= 0:
                self.value = value
            else:
                raise ValueError("<name> must be greater than 0")
        else:
            raise TypeError("<name> must be an integer")

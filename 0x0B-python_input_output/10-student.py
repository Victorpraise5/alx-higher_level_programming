#!/usr/bin/python3
"""Student to JSON with filter"""

class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """initializing data"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Function returns the dictionary description of a
        student instance """
        if type(attrs) is list and all(type(i) is str for i in attrs):
            attr_dict = {}
            for elem in attrs:
                if hasattr(self, elem):
                    attr_dict[elem] = self.__dict__[elem]
            return attr_dict
        else:
            return self.__dict__

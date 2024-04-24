#!/usr/bin/python3
"""Student to JSON"""

class Student:
    """A class that defines a student"""

    def __init__(self, first_name, last_name, age):
        """initializing data"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """to retrieve dictionary representation"""
        return self.__dict__

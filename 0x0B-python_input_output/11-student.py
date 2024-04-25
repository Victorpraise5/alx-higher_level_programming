#!/usr/bin/python3
"""Student to disk and reload"""

class Student:
    """Class student that defines a student"""

    def __init__(self, first_name, last_name, age):
        """initializing data"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary represrntation of a student instance"""
        if type(attrs) is list and all(type(i) is str for i in attrs):
            attr_dict = {}
            for elem in attrs:
                if hasattr(self, elem):
                    attr_dict[elem] = self.__dict__[elem]
            return attr_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the student instance"""
        for key, value in json.items():
            setattr(self, key, value)

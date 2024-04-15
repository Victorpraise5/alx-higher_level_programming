#!/usr/bin/python3
"""My list Module"""

class MyList(list):
    """A Class MyList that inherits from list"""

    def print_sorted(self):
        """Prints the list, but sorted"""
        sorted_list = sorted(self)
        print(sorted_list)

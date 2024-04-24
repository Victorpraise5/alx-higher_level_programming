#!/usr/bin/python3
"""Create an Object from a JSON file"""

import json

def load_from_json_file(filename):
    """creates an object from a JSON file"""
    #first open the json file using python

    with open(filename, encoding="utf-8") as my_file:
        json_data = json.load(my_file)

    return json_data

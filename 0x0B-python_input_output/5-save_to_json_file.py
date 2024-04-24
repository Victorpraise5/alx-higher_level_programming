#!/usr/bin/python3
"""Sav Object to a file"""

import json

def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using JSON representations"""
    #serialize the object to JSON format
    json_string = json.dumps(my_obj)

    with open(filename, mode='w', encoding="utf-8") as my_file:
        my_file.write(json_string)

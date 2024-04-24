#!/usr/bin/python
"""From JSON string to python object"""

import json

def from_json_string(my_str):
    """Returns an Object(Python data structure)represented by a JSON string"""
    return json.loads(my_str)

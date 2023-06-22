#!/usr/bin/python3
"""# Import Module"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Obj to a text, using JSON"""
    with open(filename, 'w') as file:
        json.dump(my_obj, file)

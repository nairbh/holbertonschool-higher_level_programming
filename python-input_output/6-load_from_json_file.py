#!/usr/bin/python3
"""# Import Module"""
import json


def load_from_json_file(filename):
    """load an Obj from json, using JSON"""

    with open(filename, 'r') as file:
        loading = json.load(file)
        return loading

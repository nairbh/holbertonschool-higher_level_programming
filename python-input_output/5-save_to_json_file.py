#!/usr/bin/python3
"""# Import Module"""


import json


def save_to_json_file(my_obj, filename):
    with open("filename", "w", encoding="UTF-8") as file:
        json.dump(my_obj, file)

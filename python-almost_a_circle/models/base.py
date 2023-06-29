#!/usr/bin/python3
"""import module"""


import json


class Base:
    """define class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """def list of dict"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            json_format = json.dumps(list_dictionaries)
            return json_format

    @classmethod
    def save_to_file(cls, list_objs):
        """ save file """
        filename = cls.__name__ + ".json"
        list_of_obj = []
        if list_objs is not None:
            for obj in list_objs:
                list_of_obj.append(obj.to_dictionary())
        with open(filename, "w", encoding="UTF-8") as file:
            file.write(cls.to_json_string(list_of_obj))

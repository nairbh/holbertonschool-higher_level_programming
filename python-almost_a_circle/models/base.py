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
        self.assertEqual(self.base.to_json_string(None), "[]")

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

    @staticmethod
    def from_json_string(json_string):
        """ from json """
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ create """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """load from file"""
        filename = cls.__name__ + ".json"
        instance_list = []
        try:
            with open(filename, "r") as file:
                json_data = file.read()
                if json_data:
                    dict_list = cls.from_json_string(json_data)
                    for item in dict_list:
                        instance = cls(**item)
                        instance_list.append(instance)
        except FileNotFoundError:
            return instance_list
        return instance_list

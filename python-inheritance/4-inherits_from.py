#!/usr/bin/python3
"""function that returns True if the objec"""


def inherits_from(obj, a_class):
    """Function that returns True if the object"""

    return issubclass(type(obj), a_class) and type(obj) != a_class

#!/usr/bin/python3
"""Write a function that returns the list of available attributes"""


def lookup(obj):
    """function that returns the list"""
    ret = dir(obj)

    if hasattr(obj, '___list__'):
        for base in obj.__list__:
            ret = ret + lookup(list)
    return ret

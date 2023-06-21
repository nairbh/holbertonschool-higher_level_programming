#!/usr/bin/python3
""" function that writes a string to a text file"""


def append_write(filename="", text=""):
    """returns the number of characters"""
    count = 0
    with open(filename, 'a', encoding='UTF8') as file:
        file.write(text)
        count = len(text)
    return count

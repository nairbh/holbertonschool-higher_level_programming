#!/usr/bin/python3
"""a function that reads a text file (UTF8) and prints it to stdout:"""


def read_file(filename=""):
    """Read file"""
    with open(filename, encoding='UTF8') as file:
        file_read = file.read()
        print(file_read, end='')

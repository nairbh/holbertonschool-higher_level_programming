#!/usr/bin/python3
def read_file(filename=""):
"""a function that reads a text file (UTF8) and prints it to stdout:"""

    with open(filename, encoding='utf-8') as f:
        text = f.read()
        print(text, end='')

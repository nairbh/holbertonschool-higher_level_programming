#!/usr/bin/python3
    """
    Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename : The name of the file to be read.

    Returns:
        None
    """
def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename : The name of the file to be read.

    Returns:
        None
    """

    with open(filename, encoding='utf-8') as f:
        text = f.read()
        print(text, end='')

#!/usr/bin/python3
"""a class MyList that inherits from list"""


class MyList(list):
    """prints the list"""

    def print_sorted(self):
        """the elements of the list will be of type int"""""
        sorted_list = sorted(self)
        print(sorted_list)

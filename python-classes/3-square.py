#!/usr/bin/python3
"""Define a class"""


class Square:

    """Define a Square"""

    def __init__(self, size=0):

        self.__size = size

        """Init Square with size = 0"""

        if not isinstance(self.__size, int):

            raise TypeError('size must be an integer')

        if size < 0:

            raise ValueError('size must be >= 0')

    def area(self):
        """Init Square area"""
        return self.__size * self.__size

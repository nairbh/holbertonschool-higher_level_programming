#!/usr/bin/python3
'''python3 -c 'print(__import__("my_module").my_function.__doc__)'''


class Square:
    '''python3 -c 'print(__import__("my_module").my_function.__doc__)'''

    def __init__(self, size=0):
        self.__size = size
        try:
            if not isinstance(self.__size, int):

                raise TypeError('size must be an integer')

            if size < 0:

                raise ValueError('size must be >= 0')

        except TypeError:
            raise TypeError('size must be >= 0')

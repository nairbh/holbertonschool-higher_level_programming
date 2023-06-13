#!/usr/bin/python3
'''defines a square'''


class Square:

    """Define a Square"""

    def __init__(self, size=0):

        '''Instantiation with optional size'''

        self.__size = size

    def area(self):
        '''returns the current square area'''
        return self.__size * self.__size

    @property
    def size(self):
        '''property def size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''setter def size'''
        if not isinstance(value, int):

            raise TypeError('size must be an integer')

        if value < 0:

            raise ValueError('size must be >= 0')

        self.__size = value

    def my_print(self):
        '''prints in stdout the square'''

        if self.size == 0:

            print()

        for i in range(self.size):
            for x in range(self.size):

                self.value = "#"
                print(self.value, end="")
            print()

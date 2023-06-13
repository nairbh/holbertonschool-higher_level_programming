#!/usr/bin/python3
'''defines a square'''


class Square:

    """Define a Square"""

    def __init__(self, size=0, position=(0, 0)):

        '''Instantiation with optional size'''

        self.__size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple or len(value) != 2:

            raise TypeError('position must be a tuple of 2 positive integers')

        self.__position = value

    def area(self):
        '''returns the current square area'''
        return self.__size * self.__size

    def my_print(self):
        if self.size == 0:
            print("")
        else:
            for i in range(self.position[1]):
                print()
            for i in range(0, self.size):
                for x in range(self.position[0]):
                    print("_", end="")
                for j in range(self.size):
                    print("#", end='')
                print()

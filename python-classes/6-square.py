#!/usr/bin/python3
'''defines a square'''


class Square:

    """Define a Square"""

    def __init__(self, size=0, position=(0, 0)):
        '''Instantiation with optional size'''
        self.size = size
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
        if not all(isinstance(num, int) and num >= 0 for num in value):
            raise ValueError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        '''returns the current square area'''
        return self.__size * self.__size

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                for _ in range(self.__position[0]):
                    print(" ", end="")
                for _ in range(self.__size):
                    print("#", end="")
                print()

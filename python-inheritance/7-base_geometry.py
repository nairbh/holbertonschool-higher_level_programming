#!/usr/bin/python3
"""a class BaseGeometry (based on 6-base_geometry.py)"""


class BaseGeometry:
    """ def class BaseGeometry """
    def area(self):
        """area define """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """ integer_validator"""

        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')

        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')

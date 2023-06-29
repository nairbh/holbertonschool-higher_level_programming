#!/usr/bin/python3
"""write a class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """def class"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """Square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        """size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update square"""
        for key, value, in kwargs.item():
            setattr(self, key, valie)
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]

    def to_dictionary(self):
        """dictionary"""
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}

#!/usr/bin/python3
"""Module defines square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update instance attributes"""
        if len(args) != 0:
            attributes = ['id', 'size', 'x', 'y']
            for count, i in enumerate(args):
                setattr(self, attributes[count], i)
        else:
            for (key, value) in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of a square"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

    def __str__(self):
        """Displays string representation"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"

#!/usr/bin/python3
"""Defines the Square class inherites Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a square class and inherits Rectangle."""

    def __init__(self, size):
        """Initializes a square with a given size."""
        super().__init__(size, size)

    def __str__(self):
        """Returns a string of the square."""
        return "[Square] {}/{}".format(self.width, self.height)

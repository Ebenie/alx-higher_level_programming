#!/usr/bin/python3
"""Defines the Square class that inherits Rectangle class"""


class Square(Rectangle):
    """A class that defines a square class"""

    def __init__(self, size):
        """Initializes a square with a given size."""
        self.integer_validator("size", size)
        super().__init__(size, size)

#!/usr/bin/python3
"""Defines the Square class inheriting from Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square class that inherits from Rectangle"""

    def __init__(self, size):
        """Initializes a square with a given size"""
        super().__init__(size, size)

    def __str__(self):
        """Returns a string representation of the square"""
        return "[Square] {}/{}".format(self.width, self.height)

    def area(self):
        """This function calculates & returns the area of the square"""
        return self.width * self.height

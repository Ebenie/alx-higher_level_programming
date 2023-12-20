#!/usr/bin/python3
"""Defines a MagicClass class."""

import math


class MagicClass:
    """Represents a MagicClass."""

    def __init__(self, radius=0):
        """Initializes a new MagicClass.

        Args:
            radius (int or float, optional): The radius of the circle.

        Raises:
            TypeError: If radius is not a number.
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculates and returns the area of the circle."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculates and returns the circumference of the circle."""
        return 2 * math.pi * self.__radius


if __name__ == "__main__":

    magic_instance = MagicClass(5)
    print("Area:", magic_instance.area())
    print("Circumference:", magic_instance.circumference())

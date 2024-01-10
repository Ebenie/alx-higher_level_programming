#!/usr/bin/python3
"""Defines the Rectangle class that inherits BaseGeometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class representing a rectangle with inherit"""

    def __init__(self, width, height):
        """Initializes a rectangle with a given width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

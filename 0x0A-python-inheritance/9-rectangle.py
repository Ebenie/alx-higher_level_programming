#!/usr/bin/python3
"""Defines the Rectangle class that inherits BaseGeometry class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class representing a rectangle."""

    def __init__(self, width, height):
        """Initializes a rectangle with a given width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """This defines Computes the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """This returns a string represents rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

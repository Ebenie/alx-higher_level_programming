#!/usr/bin/python3
"""Defines the Square class inherites Rectangle class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a square class and inherits Rectangle."""

    def __init__(self, size):
        """Initialize a new square objecect

        Args:
            size (int): The size of the new square.
        """
        super().__init__(size, size)

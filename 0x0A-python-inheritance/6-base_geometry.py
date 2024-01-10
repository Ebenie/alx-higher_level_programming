#!/usr/bin/python3
"""Defines function that checks object is an instance of class"""


class BaseGeometry:
    """An improved base geometry class based on the above"""
    
    def area(self):
        """Raises an Exception with the message 'area() is not implemented'"""
        raise Exception("area() is not implemented")

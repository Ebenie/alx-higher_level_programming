#!/usr/bin/python3
"""Defines the add_attribute function to add attribute"""


def add_attribute(obj, name, value):
    """if possible te function adds a new attribute to an object """
    if hasattr(obj, '__dict__') or (hasattr(obj, '__slots__') and name in obj.__slots__):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")

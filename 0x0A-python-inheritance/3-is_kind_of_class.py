#!/usr/bin/python3
"""Defines function that checks object is an instance of class"""


def is_kind_of_class(obj, a_class):
    """
    checks the object is instance of the specified class or inherited

    Args:
    - obj: Any Python object
    - a_class: A Python class

    Returns:
    - bool: True if obj is an instance of a_class otherwise False
    """
    return isinstance(obj, a_class)

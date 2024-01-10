#!/usr/bin/python3
"""Dfines the is_same_class function"""


def is_same_class(obj, a_class):
    """
    Check objects exactly an instance of the specified class

    Args:
    - obj: Any Python object
    - a_class: A Python class

    Returns:
    - bool: True if obj is an instance of a_class, otherwise False
    """
    return type(obj) is a_class

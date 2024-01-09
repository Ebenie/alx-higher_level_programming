#!/usr/bin/python3
"""
Module for converting class instances to JSON format.
"""

def class_to_json(obj):
    """
    Converts an object to a JSON-serializable dictionary.

    Args:
        obj: Instance of a class.

    Returns:
        dict: JSON-serializable dictionary.
    """
    return obj.__dict__


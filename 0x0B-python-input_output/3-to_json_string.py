#!/usr/bin/python3
"""
Module for returning the JSON representation of an object (string).
"""

import json


def to_json_string(my_obj):
    """
    Return the JSON representation of the given object.

    Args:
        my_obj: The object to be converted to a JSON string.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)


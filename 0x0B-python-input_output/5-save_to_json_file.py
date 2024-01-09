#!/usr/bin/python3
"""
Module for writing an Object to a text file, using a JSON representation.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Write the given object to the specified file in JSON format.

    Args:
        my_obj: The object to be written to the file.
        filename (str): The name of the file to write.

    Returns:
        None
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)


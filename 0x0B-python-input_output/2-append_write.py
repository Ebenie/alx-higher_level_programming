#!/usr/bin/python3
"""
Module for appending a string to a text file (UTF8) and returning the
number of characters written.
"""


def append_write(filename="", text=""):
    """
    Append the given text to the specified file and return the number of
    characters written.

    Args:
        filename (str): The name of the file to append to.
        text (str): The text to be appended to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)


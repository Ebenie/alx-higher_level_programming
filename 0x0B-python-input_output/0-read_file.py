#!/usr/bin/python3
"""
Module for reading a text file (UTF8) and printing its content to stdout.
"""


def read_file(filename=""):
    """
    Read the content of the given file and print it to stdout.

    Args:
        filename (str): The name of the file to read.

    Returns:
        None
    """
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")


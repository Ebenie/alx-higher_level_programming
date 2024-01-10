#!/usr/bin/python3
"""
Module for text indentation.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation_marks = ['.', '?', ':']
    buffer = ""

    for char in text:
        buffer += char
        if char in punctuation_marks:
            print(buffer.strip())
            print()
            buffer = ""

    if buffer:
        print(buffer.strip())


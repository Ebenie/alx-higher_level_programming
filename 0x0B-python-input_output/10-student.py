#!/usr/bin/python3
"""
Module for the Student class.
"""

class Student:
    """
    Represents a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new instance of the Student class.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list): List of attributes to retrieve. If None, retrieve all.

        Returns:
            dict: Dictionary representation of the Student instance.
        """
        if attrs is None or not all(isinstance(attr, str) for attr in attrs):
            return self.__dict__
        return {attr: getattr(self, attr, None) for attr in attrs}


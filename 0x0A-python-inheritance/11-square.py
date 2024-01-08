#!/usr/bin/python3

class BaseGeometry:
    """
    A class with integer validation methods.
    """
    def area(self):
        """
        Raises an Exception with the message area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value as an integer.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """
    A class representing a rectangle.
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with width and height.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Computes the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the rectangle description.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

class Square(Rectangle):
    """
    A class representing a square.
    """
    def __init__(self, size):
        """
        Initializes a Square instance with a size.
        """
        super().__init__(size, size)
        self.integer_validator("size", size)

    def __str__(self):
        """
        Returns the square description.
        """
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)


#!/usr/bin/python3
"""
Module 8-rectangle
Defines a Rectangle class with private attributes width and height.
"""


class Rectangle:
    """
    Defines the Rectangle class.
    """
    number_of_instances = 0
    syb = "#"

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance.

        Parameters:
        - width (int): The width of the rectangle.
        - height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Retrieves the width of the rectangle.

        Returns:
        int: The width of the rectangle.
        """
        return self.__wdt

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle.

        Parameters:
        value (int): The width of the rectangle.

        Raises:
        TypeError: If width is not an integer.
        ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__wdt = value

    @property
    def height(self):
        """
        Retrieves the height of the rectangle.

        Returns:
        int: The height of the rectangle.
        """
        return self.__hgt

    @height.setter
    def height(self, value):
        """
        Sets the height of the rectangle.

        Parameters:
        value (int): The height of the rectangle.

        Raises:
        TypeError: If height is not an integer.
        ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__hgt = value

    def area(self):
        """
        Calculates and returns the area of the rectangle.

        Returns:
        int: The area of the rectangle.
        """
        return self.__wdt * self.__hgt

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.

        Returns:
        int: The perimeter of the rectangle.
        """
        return 2 * (self.__wdt + self.__hgt)

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        Returns:
        str: The string representation of the rectangle.
        """
        if self.__wdt == 0 or self.__hgt == 0:
            return ""
        return "\n".join([str(self.syb)*self.__wdt for _ in range(self.__hgt)])

    def __repr__(self):
        """
        Returns a string representation of the object for debugging.

        Returns:
        str: The string representation of the object.
        """
        return "Rectangle({}, {})".format(self.__wdt, self.__hgt)

    def __del__(self):
        """
        Prints a message when an instance of Rectangle is deleted.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns the bigger rectangle based on the area.

        Parameters:
        rect_1 (Rectangle): The first rectangle.
        rect_2 (Rectangle): The second rectangle.

        Raises:
        TypeError: If rect_1 is not an instance of Rectangle.
        TypeError: If rect_2 is not an instance of Rectangle.

        Returns:
        Rectangle: The rectangle with the bigger or equal area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        area_1 = rect_1.area()
        area_2 = rect_2.area()

        if area_1 >= area_2:
            return rect_1
        else:
            return rect_2


# Testing the code
if __name__ == "__main__":
    rect1 = Rectangle(8, 4)
    rect2 = Rectangle(2, 3)

    if rect1 is Rectangle.bigger_or_equal(rect1, rect2):
        print("rect1 is bigger or equal to rect2")
    else:
        print("rect2 is bigger than rect1")

    rect2.width = 10
    rect2.height = 5
    if rect1 is Rectangle.bigger_or_equal(rect1, rect2):
        print("rect1 is bigger or equal to rect2")
    else:
        print("rect2 is bigger than rect1")

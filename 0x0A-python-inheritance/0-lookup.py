#!/usr/bin/python3

def lookup(obj):
    """
    Returns a list of attributes and methods of an object.

    Args:
    - obj: Any Python object

    Returns:
    - list: List of attribute and method names
    """
    return [n for n in dir(obj) if not callable(getattr(obj, n)) or n.startswith("__")]



class Example:
    """
    Defines the Example class to be inherited.
    """
    def __init__(self):
        self.att = 50

    def method1(self):
        return "Method 1!"

obj1 = Example()

result = lookup(obj1)
print(result)

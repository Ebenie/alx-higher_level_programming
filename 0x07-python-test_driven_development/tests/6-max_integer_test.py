#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from parameterized import parameterized  # Importing for parameterized tests
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    @parameterized.expand([
        ([1, 2, 3, 4], 4),
        ([1, 3, 4, 2], 4),
        ([], None),
        ([-1, -2, -3, -4], -1),
        ([5], 5),
        ([-5, -3, -8, -2], -2),
        ([0, 0, 0, 0], 0),
    ])
    def test_max_integer(self, input_list, expected_result):
        """Test max_integer function with different inputs"""
        result = max_integer(input_list)
        self.assertEqual(result, expected_result)

    def test_empty_list(self):
        """Test max_integer with an empty list"""
        result = max_integer([])
        self.assertIsNone(result)

    def test_float_values(self):
        """Test max_integer with float values in the list"""
        result = max_integer([1.5, 2.7, 0.3])
        self.assertEqual(result, 2.7)

    def test_invalid_list_type(self):
        """Test max_integer with invalid list type"""
        with self.assertRaises(TypeError):
            max_integer("invalid_input")

if __name__ == '__main__':
    unittest.main()


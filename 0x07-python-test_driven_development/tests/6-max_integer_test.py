#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from parameterized import parameterized
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    @parameterized.expand([
        ([1, 2, 3, 4], 4),
        ([1, 3, 4, 2], 4),
        ([], None),
        ([7], 7),
        ([5, 5, 5, 5], 5),
        ([-1, -2, -3, -4], -1),
        ([-4, -3, -2, -1], -1),
        ([10, -10, 5, -5], 10),
        ([0, 0, 0, 0], 0),
    ])
    def test_max_integer(self, input_list, expected_result):
        result = max_integer(input_list)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()


#!/usr/bin/python3
"""Module to perform lazy matrix multiplication using NumPy
"""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Function to multiply two matrices using NumPy"""
    if not isinstance(m_a, list) or not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if not isinstance(m_b, list) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not m_a or any(not row for row in m_a):
        raise ValueError("m_a can't be empty")

    if not m_b or any(not row for row in m_b):
        raise ValueError("m_b can't be empty")

    if any(not isinstance(elem, (int, float)) for row in m_a for elem in row):
        raise TypeError("m_a should contain only integers or floats")

    if any(not isinstance(elem, (int, float)) for row in m_b for elem in row):
        raise TypeError("m_b should contain only integers or floats")

    if any(len(row) != len(m_a[0]) for row in m_a):
        raise ValueError("each row of m_a must be of the same size")

    if any(len(row) != len(m_b[0]) for row in m_b):
        raise ValueError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = np.dot(np.array(m_a), np.array(m_b))
    return result.tolist()


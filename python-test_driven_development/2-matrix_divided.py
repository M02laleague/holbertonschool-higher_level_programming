#!/usr/bin/python3
"""
This module contains a function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    This function divides all elements of a matrix
    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(matrix[0]) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")
    for row in matrix:
        for element in row:
            if type(element) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    return [[round(element / div, 2) for element in row] for row in matrix]
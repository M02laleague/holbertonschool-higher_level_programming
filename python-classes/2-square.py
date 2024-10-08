#!/usr/bin/python3
"""
This module defines a Square class with a private instance attribute 'size'.
The size must be an integer and greater than or equal to 0.
"""


class Square:
    """Represents a square with a specific size."""
    def __init__(self, size=0):
        """
        Initializes the square with a specific size.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

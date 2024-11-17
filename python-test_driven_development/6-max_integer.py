#!/usr/bin/python3
"""
This module contains a function that finds the max integer in a list
"""


def max_integer(list=[]):
    """
    This function finds the max integer in a list
    """
    if len(list) == 0:
        return None
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max
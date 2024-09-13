#!/usr/bin/python3
def add_integer(a, b=98):
    """Adds two integers or floats and returns the result as an integer."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    # Convert both to integers
    a = int(a)
    b = int(b)
    return a + b

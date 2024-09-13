#!/usr/bin/python3
def text_indentation(text):
    """Prints text with two new lines after each of these characters: ., ?, :."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    special_chars = ['.', '?', ':']
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in special_chars:
            print("\n")
        i += 1

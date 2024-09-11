#!/usr/bin/python3
def no_c(my_string):
    """Retourne une nouvelle chaîne sans les caractères 'c' et 'C'."""
    return my_string.translate({ord('c'): None, ord('C'): None})

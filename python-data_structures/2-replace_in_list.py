#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Remplace l'élément à l'indice idx par un nouvel élément."""
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
    return my_list

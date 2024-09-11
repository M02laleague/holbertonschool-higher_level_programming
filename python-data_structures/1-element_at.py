#!/usr/bin/python3
def element_at(my_list, idx):
    """Retourne l'élément à l'indice idx d'une liste."""
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]

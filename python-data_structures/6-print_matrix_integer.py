#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Affiche une matrice d'entiers."""
    for row in matrix:
        print(" ".join("{:d}".format(x) for x in row))

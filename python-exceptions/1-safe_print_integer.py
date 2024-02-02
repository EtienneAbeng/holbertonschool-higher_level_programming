#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))  # Essaye d'imprimer la valeur comme un entier
        return True  # Retourne True si l'impression réussit
    except (TypeError, ValueError):
        return False  # Retourne False en cas d'erreur de type ou de valeur

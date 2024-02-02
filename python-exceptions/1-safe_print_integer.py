!/usr/bin/python3

def safe_print_integer(value):
    try:
        # Utilise "{:d}".format() pour imprimer l'entier
        print("{:d}".format(value))
        # Si l'impression réussit, retourne True
        return True
    except (ValueError, TypeError):
        # En cas d'erreur (ValueError ou TypeError), retourne False
        return False

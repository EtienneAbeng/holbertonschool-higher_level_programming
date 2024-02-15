#!/usr/bin/python3
"""
Une fonction qui retourne True si l'object est exactement une instance
de la class spécifié sinoon retourne True
"""


def is_same_class(obj, a_class):
    """Verifie si l'objet est une instance de la classe spécifiée"""
    # Utilisation de isinstance pour vérifier si l'objet est une instance

    return type(obj) is a_class

#!/usr/bin/python3

def is_same_class(obj, a_class):
    """Verifie si l'objet est une instance de la classe spécifiée"""
    # Utilisation de isinstance pour vérifier si l'objet est une instance

    return type(obj) is a_class

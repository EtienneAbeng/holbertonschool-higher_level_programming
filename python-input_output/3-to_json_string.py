#!/usr/bin/python3
"""
Ce script contient une fonction qui retourne la représentation JSON d'un objet.
"""

import json


def to_json_string(my_obj):
    """
    Convertit un objet Python en une chaîne JSON.

    Args:
        my_obj: L'objet Python à convertir en JSON.

    Returns:
           La représentation JSON de l'objet en tant que chaîne.
    """
    json_str = json.dumps(my_obj)
    # Utiliser json.dumps pour convertir l'objet en une chaîne JSON
    return json_str

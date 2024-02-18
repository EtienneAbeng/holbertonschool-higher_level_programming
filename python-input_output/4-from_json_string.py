#!usr/bin/python3
"""
 Le script écrit une foction qui retourne un objet (Python data structure)
 qui represente un Jsonstring
"""
import json


def from_json_string(my_str):
    """
    Convertit une chaîne JSON en un objet Python.

    Args:
        my_str (str): La chaîne JSON à convertir.

    Returns:
        object: L'objet Python résultant de la désérialisation.
    """
    data_struct = json.loads(my_str)

    return data_struct

#!/usr/bin/python3
"""
le script contient une fonction pour charger un objet Python 
depuis un fichier JSON.
"""
import json


def load_from_json_file(filename):
    """
    Charge un objet Python depuis un fichier JSON.

    Args:
        filename: Le nom du fichier JSON à charger.

    Returns:
        object: L'objet Python résultant de la désérialisation.
    """
    # Ouvre le fichier JSON en mode lecture
    with open(filename, "r", encoding="utf-8") as f:
        # Charge le contenu du fichier en tant qu'objet Python
        objet_python = json.load(f)
        return objet_python

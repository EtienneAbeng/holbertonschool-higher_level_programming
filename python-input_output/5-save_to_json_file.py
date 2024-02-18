#!/usr/bin/python3
"""
Écrire une fonction qui écrit un objet dans un fichier texte,
en utilisant une représentation JSON
"""
import json

def save_to_json_file(my_obj, filename):
    """
    Sauvegarde un objet Python dans un fichier JSON.

    Args:
        my_obj: L'objet Python à sauvegarder.
        filename (str): Le nom du fichier de sortie.

    Returns:
        None
    """
    with open(filename, "w", encoding="utf-8") as outfile:
        json.dump(my_obj, outfile)

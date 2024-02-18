#!/usr/bin/python3
"""
    Le script écrit dans le fichier et retourne le chiffre de caractére
"""
def write_file(filename="", text=""):
    """Écrit une chaîne de caractères dans un fichier texte (UTF-8) et retourne le nombre de caractères écrits.

    Args:
        filename : Le chemin vers le fichier à écrire
        text : La chaîne de caractères à écrire dans le fichier

    Returns:
        int: Le nombre de caractères écrits dans le fichier.

    """
    # Ouvre le fichier pour écrire avec l'encodage UTF-8
    with open(filename, "w", encoding="utf-8") as f:
        # Écrire dans le fichier
        nb_characters = f.write(text)
    # Retourne le nombre de caractères écrits dans le fichier
    return nb_characters

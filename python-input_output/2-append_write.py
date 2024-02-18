#!/usr/bin/python3
"""
Le script ajoute une chaine de caractére en toute fin du fichier
"""


def append_write(filename="", text=""):
    """
    Args :
        filename: le chemin vers le fichier à modifier
    Return:
        retourne le nombre de caractére ajoutés en plus au fichier grâce à write
    """
    # Ouvre le fichier en mode ajout avec "a" avec l'encodage
    with open(filename, "a", encoding="utf-8") as f:
        #Ecrire à la fin du fichier la chaine de caractére
        nb_char_app = f.write(text)
        # Retourne le nombre de caractére affichait à la fin du fichier
        return nb_char_app

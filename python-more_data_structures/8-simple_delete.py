#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):

    # Vérifie si le dictionnaire est None
    if a_dictionary is None:
        return None

    # Vérifie si la clé existe dans le dictionnaire
    if key in a_dictionary:
        # Supprime la clé si elle existe
        del a_dictionary[key]

    # Retourne le dictionnaire après la suppression ou sans modification si la clé n'existait pas
    return a_dictionary

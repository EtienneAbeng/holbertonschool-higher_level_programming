#!/usr/bin/python3

def number_keys(a_dictionary):

    # Vérifier si le dictionnaire est None
    if a_dictionary is None:
        return 0

    # Utiliser len() pour obtenir le nombre de clés dans le dictionnaire
    nb_keys = len(a_dictionary.keys())
    return nb_keys

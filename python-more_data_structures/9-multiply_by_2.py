#!/usr/bin/python3

def multiply_by_2(a_dictionary)

    # Vérifie si le dictionnaire est None
    if a_dictionary is None:
        return None

    # Crée une copie du dictionnaire
    new_dict = a_dictionary.copy()

    # Parcourt chaque clé du dictionnaire
    for key in new_dict:
        # Multiplie la valeur de chaque clé par 2
        new_dict[key] *= 2

    # Retourne le nouveau dictionnaire modifié
    return new_dict

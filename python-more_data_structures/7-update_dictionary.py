#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    # Vérifier si le dictionnaire est None
    if a_dictionary is None:
        return None

    # Si la clé existe dans le dictionnaire, mettre à jour la valeur
    if key in a_dictionary:
        a_dictionary[key] = value
    else:
        # Si la clé n'existe pas, ajouter une nouvelle paire clé-valeur
        a_dictionary[key] = value

    return a_dictionary

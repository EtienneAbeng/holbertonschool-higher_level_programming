#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    # Vérifier si le dictionnaire est None
    if a_dictionary is None:
        return None

    # Utiliser la fonction sorted() pour obtenir une liste triée des clés
    sorted_keys = sorted(a_dictionary.keys())

    # Parcourir les clés triées et afficher chaque paire clé-valeur
    for key in sorted_keys:
        value = a_dictionary[key]
        print("{}: {}".format(key, value))

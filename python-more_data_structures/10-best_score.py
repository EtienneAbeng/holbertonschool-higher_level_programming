#!/usr/bin/python3

def best_score(a_dictionary):
    # Vérifie si le dictionnaire est None ou vide
    if a_dictionary is None or not a_dictionary:
        return None

    # la fonction max() avec get pour trouver la clé avec la plus grande valeur
    # Cette méthode prend la clé correspondant à la plus grande valeur
    best_key = max(a_dictionary, key=a_dictionary.get)

    # Retourne la meilleure clé
    return best_key


#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # Utilise une expression de dictionnaire afin créer un nouveau dictionnaire
    # où chaque valeur est multipliée par 2
    new_dictionary = {key: value * 2 for key, value in a_dictionary.items()}
    return new_dictionary  # Retourne le nouveau dictionnaire


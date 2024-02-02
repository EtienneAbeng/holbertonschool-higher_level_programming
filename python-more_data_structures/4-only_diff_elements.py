#!/usr/bin/python3

def only_diff_elements(set_1, set_2):

    # Vérifier si l'un des ensembles est None
    if set_1 is None or set_2 is None:
        return None

    # operateur ^ pour obtenir les éléments présents dans un seul ensemble
    return set_1 ^ set_2

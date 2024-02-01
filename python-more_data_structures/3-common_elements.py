#!/usr/bin/python3

def common_elements(set_1, set_2):
    # Vérifier si l'un des ensembles est None
    if set_1 is None or set_2 is None:
        return None

    # Retourner l'ensemble des éléments communs
    return set_1 & set_2

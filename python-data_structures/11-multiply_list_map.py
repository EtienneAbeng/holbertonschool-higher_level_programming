#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # Vérifie si l'indice (idx) est dans la plage valide
    if idx >= 0 and idx < len(my_list):
        # Supprime l'élément à l'indice donné
        del my_list[idx]

    # Retourne la liste mise à jour
    return my_list

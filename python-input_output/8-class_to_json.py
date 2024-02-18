#!/usr/bin/python3
"""
Convertit une instance de classe en un dictionnaire 
pour la sérialisation JSON.
"""

def class_to_json(obj):
    """
    Convertit une instance de classe en un dictionnaire 
    pour la sérialisation JSON.

    Args:
        obj: L'instance de classe à convertir.

    Returns:
        dict: Le dictionnaire représentant l'instance de classe.
    """
    # Initialise un dictionnaire vide pour stocker les attributs de l'objet
    obj_dict = {}

    # Récupère tous les attributs de l'objet
    attributes = vars(obj)

    # Parcourt chaque attribut de l'objet
    for attr, value in attributes.items():
        # Vérifie si la valeur de l'attribut est un type  sérialisable JSON
        if isinstance(value, (list, dict, str, int, bool)):
            # Ajoute l'attribut et sa valeur correspondante au dictionnaire
            obj_dict[attr] = value

    return obj_dict

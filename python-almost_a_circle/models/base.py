#!/usr/bin/python3
"""
   Ce script créer une classe Base qui gère l'attributioni dentifiant uniques
   L'identifiant est soit fourni lors de l'instanciation, soit auto-incrémenté
"""
import json

class Base:
    """
    Classe de basse pour gérer les identifiants uniques des instances
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructeur de la class Base

        Args:
        id (int): Si l'instance est donnée, il est utilisé sinon on incrémente
        avec l'instance de class privée
        """

        if id is not None:  # si id est donnée
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects  # incrementation et assignation

def to_json_string(list_dictionaries):
    """
    Convertit une liste de dictionnaires en chaîne JSON

    Args:
        list_dictionaries (list): Liste de dictionnaires à convertir

    Returns:
        str: Chaîne JSON représentant la liste de dictionnaires
    """
    if list_dictionaries is None:
        # Si list_dictionaries est None, aucun argument n'a été passé à la fonction
        # Nous retournons une chaîne JSON vide dans ce cas.
        return "[]"
    elif len(list_dictionaries) == 0:
        # Si list_dictionaries est une liste vide, aucun dictionnaire présent dans la liste
        # Nous retournons également une chaîne JSON vide dans ce cas.
        return "[]"
    else:
        # Utiliser la fonction json.dumps() pour convertir la liste de dictionnaires en chaîne JSON
        return json.dumps(list_dictionaries)


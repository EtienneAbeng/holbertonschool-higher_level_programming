#!/usr/bin/python3
"""
   Ce script créer une classe Base qui gère l'attributioni dentifiant uniques
   L'identifiant est soit fourni lors de l'instanciation, soit auto-incrémenté
"""


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

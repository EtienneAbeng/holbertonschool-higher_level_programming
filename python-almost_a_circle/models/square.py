#!/usr/bin/python3
from models/rectangle import Rectangle


class Square(Rectangle):
    """
    Initialise une instance de square

    Args:
        Size(int): Taille du carré

        x : Coordonnée x du carré
        y : Cordonnée y du carré
        id : L'identité du carré
    """


    def __init__(self, size, x=0, y=0, id=None):

        super.()__init__(size, size, width, height, id)

    @property

    def size(self):
        """Obtenir la taille du carré"""
        return self.width

    @size.setter
    def size(self, value):
        """Définir la taille du carré"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Mettre les attributs du carré à jour

        Args: 
            *args: Arguments sans mot cle
            **kwargs: Arguments avec mot clé
        """

        if arg

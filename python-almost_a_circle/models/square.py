#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    """Classe Square hérite de Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialise une instance de carré.

        Args:
            size (int): Taille du carré.
            x (int): Coordonnée x du coin supérieur gauche du carré.
            y (int): Coordonnée y du coin supérieur gauche du carré.
            id (int): Identifiant du carré.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Renvoie une représentation sous forme de chaîne de caractères du carré.

        Returns:
            str: Une représentation sous forme de chaîne de caractères du carré.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Obtient la taille du carré."""
        return self.width

    @size.setter
    def size(self, value):
        """Définit la taille du carré."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Met à jour les attributs du carré.

        Args:
            *args: Arguments sans mot-clé.
            **kwargs: Arguments avec mot-clé.
        """
        if args:
            attrs = ["id", "size", "x", "y"]  # Liste d'attributs aux arguments sans mot-clé
            for i, arg in enumerate(args):  # Itérer sur les arguments sans mot-clé
                setattr(self, attrs[i], arg)  # Définir dynamiquement chaque attribut du carré
        else:  # Si aucun argument sans mot-clé n'est fourni
            for key, value in kwargs.items():  # Itérer sur les arguments avec mot-clé
                setattr(self, key, value)  # Définir dynamiquement en utilisant les arguments avec mot-clé

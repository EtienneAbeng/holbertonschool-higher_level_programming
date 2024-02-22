#!/usr/bin/python3

from models.rectangle import Rectangle

class Square(Rectangle):
    """Class Square hérite de Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialise une instance de carré."""
        super().__init__(size, size, x, y, id)  # Appel du constructeur de la classe Rectangle avec la même taille pour width et height

    def __str__(self):
        """Renvoie une représentation sous forme de chaîne de caractères du carré."""
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
        if args:  # Si des arguments sont fournis sous forme de tuple
            attrs = ["id", "size", "x", "y"]  # Liste des attributs dans l'ordre attendu
            for i, arg in enumerate(args):  # Parcours des arguments
                setattr(self, attrs[i], arg)  # Affectation des valeurs aux attributs correspondants
        else:
            for key, value in kwargs.items():  # Parcours des arguments clé-valeur
                setattr(self, key, value)  # Affectation des valeurs aux attributs correspondants

    def to_dictionary(self):
        """
        Renvoie une représentation sous forme de dictionnaire du carré.

        Returns:
            dict: Une représentation sous forme de dictionnaire du carré.
        """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}  # Affiche dictionnaire du carré

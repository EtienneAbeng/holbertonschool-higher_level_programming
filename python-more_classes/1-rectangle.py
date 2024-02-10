#!/usr/bin/python3

'''
Le script definit une classe rectangle pour representer ce rectangle
La class a 2 attributs privée __height et __weight du rectangle
Les méthodes de propriété pour récupérer sont getter et setter
'''

#!/usr/bin/python3
"""Définit un rectangle vide."""


class Rectangle:
    """Représente un rectangle vide."""

    def __init__(self, width=0, height=0):
        """Initialise le rectangle avec une largeur et une hauteur."""
        self.height = height  # Initialisation de la hauteur
        self.width = width  # Initialisation de la largeur

    @property
    def width(self):
        """Getter pour récupérer la largeur du rectangle."""
        return self.__width  # Retourne la largeur du rectangle

    @width.setter
    def width(self, value):
        """Setter pour définir la largeur du rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")  # Vérifie si c'est un entier
        if value < 0:
            raise ValueError("width must be >= 0")  # Vérifie si c'est positif
        self.__width = value  # Définit la largeur du rectangle

    @property
    def height(self):
        """Getter pour récupérer la hauteur du rectangle."""
        return self.__height  # Retourne la hauteur du rectangle

    @height.setter
    def height(self, value):
        """Setter pour définir la hauteur du rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")  # Vérifie si c'est un entier
        if value < 0:
            raise ValueError("height must be >= 0")  # Vérifie si c'est positif
        self.__height = value  # Définit la hauteur du rectangle

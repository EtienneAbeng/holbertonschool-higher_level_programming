#!/usr/bin/python3
from models.base import Base
""" Importation du module Base se trouvant dans le dossier models"""


class Rectangle(Base):
    """Classe Rectangle hérite de class Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialise une instance de rectangle

        Args:
            width (int): Largeur du rectangle
            height (int): Hauteur du rectangle
            x (int): Position x
            y (int): Position y
            id (int): Identifiant du rectangle
        """
        # Appel le constructeur de la class parent(base) avec super
        super().__init__(id)
        # Initialise les attributs de rectangle
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property  # définir un accesseur (getter) pour un attribut de class
    def width(self):
        """Acceseur pour la largeur"""
        return self.__width

    @width.setter  # définir un mutateur permet de modifier la largeur
    def width(self, value):
        """Mutateur pour la largeur"""
        if is not isinstance(value, int):
            raise TypeError("width must be an integer")

        elif value <= 0:
            raise ValueError("width must > 0")

        else:
            self.__width = value

    @property  # définir un accesseur (getter) pour un attribut de class
    def height(self):
        """Accesseur pour la hauteur"""
        return self.__height

    @height.setter  # définir un mutateur permettant de modifier la hauteur
    def height(self, value):
        """Mutateur pour la hauteur"""
        if is not isinstance(value, int):
            raise TypeError("height must be an integer")

        elif value <= 0:
            raise ValueError("height must > 0")

        else:
            self.__height = value

    @property  # définir un acesseur (getter) pour un attribut class
    def x(self):
        """ Accesseur de coordonnée x"""
        return self.__x

    @x.setter  # définir un mutateur permet de modifier la coordonnée x
    def x(self, value):
        """Mutateur de coordonnée x"""
        if is not isinstance(value, int):
            raise TypeError("x must be an integer")

        elif value <= 0:
            raise ValueError("x must be > 0")
        else:
            self.__x = value

    @property  # définier un mutateur (getter) pour un attribut class
    def y(self):
        """Acceseur de coordonneé y"""
        return self.__y

    @y.setter  # définir un mutateur permet de modifier la coordonnée y
    def y(self, value):
        """Mutateur"""
        if is not isinstance(value, int):
            raise TypeError("y must be an integer")

        elif value <= 0:
            raise ValueError("y must be >= 0")

        else:
            self.__y = value

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
        self.__width = value

    @property  # définir un accesseur (getter) pour un attribut de class
    def height(self):
        """Accesseur pour la hauteur"""
        return self.height

    @height.setter  # définir un mutateur permettant de modifier la hauteur
    def height(self, value):
        """Mutateur pour la hauteur"""
        self.__width = value

    @property  # définir un acesseur (getter) pour un attribut class
    def x(self):
        """ Accesseur de coordonnée x"""
        return self.__x

    @x.setter  # définir un mutateur permet de modifier la coordonnée x
    def x(self, value_x):
        """Mutateur de coordonnée x"""
        self.__x = value_x

    @property  # définier un mutateur (getter) pour un attribut class
    def y(self):
        """Acceseur de coordonneé y"""
        return (self)

    @y.setter  # définir un mutateur permet de modifier la coordonnée y
    def y(self, value_y):
        """Mutateur"""
        self.__y = value_y

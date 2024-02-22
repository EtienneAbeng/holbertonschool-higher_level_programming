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
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property  # définir un accesseur (getter) pour un attribut de class
    def width(self):
        """Acceseur pour la largeur"""
        return self.__width

    @width.setter  # définir un mutateur permet de modifier la largeur
    def width(self, value):
        """Mutateur pour la largeur"""
        if not isinstance(value, int):
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
        if not isinstance(value, int):
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
        if not isinstance(value, int):
            raise TypeError("x must be an integer")

        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property  # définier un mutateur (getter) pour un attribut class
    def y(self):
        """Acceseur de coordonneé y"""
        return self.__y

    @y.setter  # définir un mutateur permet de modifier la coordonnée y
    def y(self, value):
        """Mutateur"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")

        elif value < 0:
            raise ValueError("y must be >= 0")

        else:
            self.__y = value

    def area(self):
        """Calcule l'air d'un rectangle"""
        return self.width * self.height  # Largeur * hauteur

    def display(self):
        """
        Affiche le Rectangle en stdout avec  '#' en prenant compte de x et y
        """
        for _ in range(self.y):  # Se déplace sur abscisse y
            print()
        for _ in range(self.height):  # Se place sur l hauteur
            # Imprime en 1 des espaces vide puis une concatenation rajoute des
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Renvoie une chaîne de caractères représentant l'instance Rectangle

        Le format sera : [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
        Assigne chaque argument à un attribut

        Args:
            *args: Arguments à assigner aux attributs, dans l'ordre suivant
               1. id, 2. width, 3. height, 4. x, 5. y
        """

        if args and len(args) > 0:
            attrs = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args[:5]):
                setattr(self, attrs[i], arg)
        elif kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionnary(self):
	"""
	Return representation d'un dictionnaire d'un rectangle
	"""
	return {'id': self.id, 'size': self.size, 'x':size.x, 'y': size.y}

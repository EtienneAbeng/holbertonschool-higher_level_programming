#!/usr/bin/python3
"""
Ce script démontre l'utilisation d'une classe BaseGeometry avec une méthode area()
afin de calculer l'air d'un rectangle
"""


class BaseGeometry:
    """
    Une base class qui représente une géometrie.

    Methods:
    area(self): Calcule l'aire de la géométrie
        léve une exception car elle n'est pas impléentée dans la class de base
    """

    def area(self):
        """
        Calcule l'aire d'un rectangle

        Raises:
            Exception: La méthode ne se trouve pas dans la base de class
        """
        # Lève une exception car le calcul de l'aire 
        # n'est pas implémenté dans la classe de base
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Valide si la valeur passé est bien en entier

        Args:
            TypeError: Verifie si la valeur reçu est le bon type

            ValueError: Verifie si la valeur reçu est un entier postive
        """
        # La fonction isinstance permet de vérifier le type d'objet d'une variable. 
        # Prend en argument la variable à étudier et le type d'objet à vérifier. 
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """La class rectangle hérite de tout les attributs et class 
        de BaseGeometry
    """

    def __init__(self, width, height):

        self.__width = width
        self.__height = height
        self.integer_validator = ("width", width)
        self.integer_validator = ("height", height)

    def __str__(self):
        """
        Returns :
            str : Une représentation d'une chaîne caractères du rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """
        Calcule et retourne la valeur de l'aire d'un rectangle,
        en multipliant largeur * hauteur
        """
        return self.__width * self.__height


#!/usr/bin/python3
"""
Ce script démontre l'utilisation d'une classe BaseGeometry avec une méthode area()
qui lève une exception lorsqu'elle est appelée sans être implémentée.
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

#!/usr/bin/python3
""" Le script définis la fonction is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """Verifie si l'objet est une instance de la classe specifée
       ou d'une classe qui hérite de celle ci

    Args:
        obj: L'objet à vérifier
        a_class: La classe à comparer

    Return:
        True is l'objet est une instance de la classe specifiée
        ou d'une classe qui hérite de celle-ci sinon False
    """
    if isinstance(obj, a_class):

        return True

    else:
        return False

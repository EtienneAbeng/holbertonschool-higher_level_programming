#!/usr/bin/python3

"""Le script vérifie si un objet est une instance d'une classe qui hérite
directement ou indirect avec issubclass
"""


def inherits_from(obj, a_class):
    """Vérifie si l'objet est une instance d'une classe qui a hérité
       (directement ou indirectement) de la classe spécifié

    Args:
        obj: L'objet à vérifier
        a_class: la class spécifié à comparer

    Return:
        True si l'objet est une instance d'une classe qui a hérité
        sinon rtourne False
    """
    
    #Vérifie si le type de l'objet est une sous classe de la classe spécifié
    if issubclass(type(obj), a_class):  # Bien rajouter type, important

        return True
    else:
        return False

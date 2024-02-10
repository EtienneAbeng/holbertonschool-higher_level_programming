#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    '''
     Importe argv du module sys, qui la liste 
     des arguments de la ligne de commande.
    '''

    args = len(argv) - 1

    '''
     Calcule le nombre d'arguments en soustrayant -1 
    de la longueur de argv (le nom du script est inclus).
    '''

    if args == 0:
        print("{} arguments.".format(args))
        # S'il n'y a aucun argument, affiche "0 arguments."
    elif args == 1:
        print("{} argument:".format(args))
        # S'il y a un seul argument, affiche "1 argument:"
    else:
        print("{} arguments:".format(args))
        # Si le nombre d'arguments est supérieur à 1, affiche "{} arguments:"

    for i in range(args):
        # Boucle pour chaque argument à partir de l'indice 0 jusqu'à args - 1.
        print("{}: {}".format(i + 1, argv[i + 1]))
        # Affiche la position de l'argument et sa valeur.

#!/usr/bin/python3
"""Affiche toutes les valeurs dans la table des états où le nom correspond à l'argument"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Paramètres de connexion à la base de donnees
    username = sys.argv[1]    # Nom d'utilisateur MySQL
    password = sys.argv[2]    # Mot de passe MySQL
    database= sys.argv[3]     # Nom de la base de données MySQL
    

    # Connexion à la base de données MySQL
    db = MySQLdb.connect(
        host='localhost',       # Adresse de l'hôte MySQL
        port=3306,              # Port MySQL
        user=username,         # Nom d'utilisateur MySQL
        passwd=password,       # Mot de passe MySQL
        db=database,            # Nom de la base de données MySQL
        charset='utf8'         # Encodage UTF-8
    )

    # Creation d'un objet curseur pour executer des requêtes SQL
    cursor = db.cursor()

    try:
        # Preparation de la requête SQL pour sélectionner les états où le nom correspond à l'argument

    # Execution de la requête SQL pour obtenir tous les états commençant par 'N'
    # LIKE est utilisé pour rechercher des correspondances partielles dans les chaînes de caractères
    # Le '%' est un caractère générique qui représente zéro ou plusieurs caractères.
    # Le mot-clé BINARY spécifie que la comparaison des chaînes de caractères doit être sensible à la casse
        sql_query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(state_name)

        # Exécution de la requête SQL
        cursor.execute(sql_query)

        # Récupération de tous les résultats de la requête
        results = cursor.fetchall()

        # Affichage des résultats
        for row in results:  # Parcours chaque ligne de la table states retournee par la requête
            print(row)       # Affiche chaque ligne de résultat


    except Exception as e:
        # Gestion des erreurs
        print("Erreur:", e)

    finally:
        # Fermeture de la connexion à la base de donnees
        db.close()
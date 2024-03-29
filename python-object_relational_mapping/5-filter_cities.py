#!/usr/bin/python3
"""Affiche toutes les valeurs dans la table des états où le nom correspond à l'argument"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Paramètres de connexion à la base de données
    username = sys.argv[1]    # Nom d'utilisateur MySQL
    password = sys.argv[2]    # Mot de passe MySQL
    database = sys.argv[3]    # Nom de la base de données MySQL
    state_name = sys.argv[4]  # Nom de l'état recherché

    try:
        # Connexion à la base de données MySQL
        db = MySQLdb.connect(
            host='localhost',       # Adresse de l'hôte MySQL
            port=3306,              # Port MySQL
            user=username,         # Nom d'utilisateur MySQL
            passwd=password,       # Mot de passe MySQL
            db=database,            # Nom de la base de données MySQL
            charset='utf8'         # Encodage UTF-8
        )

        # Création d'un objet curseur pour exécuter des requêtes SQL
        cursor = db.cursor()

        # Utilisation d'un INNER JOIN pour combiner les données de deux tables en fonction d'une condition de jointure.

        # Le mot-clé BINARY spécifie que la comparaison des chaînes de caractères doit être sensible à la casse
        # Préparation de la requête SQL avec un paramètre de requête sécurisé
        sql_query = "SELECT cities.id, states.name " \
                    "FROM cities JOIN states ON cities.state_id = states.id " \
                    "WHERE states.name LIKE BINARY %s ORDER BY cities.id ASC"

        # Exécution de la requête SQL avec le paramètre sécurisé
        cursor.execute(sql_query, (state_name + '%',))

        # Récupération de tous les résultats de la requête
        results = cursor.fetchall()

        # Affichage des résultats
        cities = [row[1] for row in results]
        if cities:
            print(", ".join(cities))
        else:
            print("No cities found:", state_name)

    except MySQLdb.Error as e:
        # Gestion des erreurs MySQL
        print("Error:", e)

    except Exception as e:
        # Gestion des autres erreurs
        print("Error:", e)

    finally:
        # Fermeture de la connexion à la base de données
        if 'db' in locals() and db:
            cursor.close()
            db.close()

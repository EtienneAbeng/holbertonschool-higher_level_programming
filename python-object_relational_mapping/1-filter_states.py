#!/usr/bin/python3
"""Ce script liste tous les états de la base de données hbtn_0e_0_usa."""

import MySQLdb  # Importation du module MySQLdb pour interagir avec la base de données
import sys  # Importation du module sys pour accéder aux arguments de ligne de commande

if __name__ == "__main__":
    # Paramètres de connexion à la base de données
    username = sys.argv[1]  # Nom d'utilisateur MySQL
    password = sys.argv[2]  # Mot de passe MySQL
    database = sys.argv[3]  # Nom de la base de données MySQL

    # Connexion au serveur MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Création d'un curseur pour exécuter des requêtes SQL
    cursor = db.cursor()

    # Exécution de la requête SQL pour obtenir tous les états
    cursor.execute("SELECT * FROM states WHERE name LIKE NINARY ORDER BY id ASC")

    # Récupération de tous les résultats
    results = cursor.fetchall()

    # Affichage des résultats
    for row in results:
        print(row)

    # Fermeture du curseur et de la connexion à la base de données
    cursor.close()
    db.close()

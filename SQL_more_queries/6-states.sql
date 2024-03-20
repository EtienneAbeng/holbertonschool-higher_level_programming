-- <CREATE DATABASE IF NOT EXISTS> Crée une nouvelle base de données si elle n'existe pas déjà
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- <CREATE TABLE> Crée une nouvelle table dans la base de données hbtn_0d_usa si elle n'existe pas déjà
-- <UNIQUE> La contrainte UNIQUE garantit qu'aucune valeur en double n'est autorisée dans la colonne où elle est appliquée. Dans ce cas, la colonne id ne peut pas contenir de doublons.
-- <AUTO_INCREMENT> Lorsqu'une nouvelle ligne est insérée dans la table, la valeur de la colonne auto-incrémentée (ici id) est automatiquement augmentée d'une unité sans nécessiter de spécification explicite de sa valeur

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT AUTO_INCREMENT UNIQUE,  -- Crée une colonne id de type INT auto-incrémentée et unique
    name VARCHAR(256),  -- <VARCHAR> Crée une colonne name de type VARCHAR avec une longueur maximale de 256 caractères
    PRIMARY KEY (id)  -- <PRIMARY KEY> Définit la colonne id comme clé primaire de la table
);

-- <CREATE DATABASE IF NOT EXISTS> Crée une nouvelle base de données si elle n'existe pas déjà
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- <CREATE TABLE IF NOT EXISTS> Crée une nouvelle table dans la base de données hbtn_0d_usa si elle n'existe pas déjà
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT AUTO_INCREMENT UNIQUE,  -- <AUTO_INCREMENT> Crée une colonne id de type INT auto-incrémentée et unique
    state_id INT NOT NULL,  -- Crée une colonne state_id de type INT qui ne peut pas être nulle
    name VARCHAR(256) NOT NULL,  -- <VARCHAR> Crée une colonne name de type VARCHAR avec une longueur maximale de 256 caractères, qui ne peut pas être nulle
    PRIMARY KEY (id),  -- <PRIMARY KEY> Définit la colonne id comme clé primaire de la table
    FOREIGN KEY (state_id) REFERENCES states(id)  -- Crée une contrainte <FOREIGN KEY> pour lier la colonne state_id à la colonne id de la table states
);

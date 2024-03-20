-- <CREATE DATABASE> Créer la base de données hbtn_0d_2 si elle n'existe pas déjà
CREATE DATABASE 
    IF NOT EXISTS hbtn_0d_2;

-- <CREATE USER> Crée un nouvel utilisateur s'il n'existe pas déjà, sur le localhost
-- <IDENTIFIED BY> Définit un mot de passe pour le nouvel utilisateur
CREATE USER 
    IF NOT EXISTS 'user_0d_2'@'localhost'
    IDENTIFIED BY 'user_0d_2_pwd';

-- Accorder le privilège SELECT sur toutes les tables dans la base de données hbtn_0d_2 à l'utilisateur user_0d_2
GRANT SELECT
    ON hbtn_0d_2.*  -- Accorde le privilège SELECT sur toutes les tables dans la base de données hbtn_0d_2
    TO 'user_0d_2'@'localhost';

-- <FLUSH PRIVILEGES> permet de recharger les privilèges et d'appliquer les modifications des droits.
FLUSH PRIVILEGES;

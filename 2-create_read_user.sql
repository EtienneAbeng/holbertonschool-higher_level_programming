-- <CREATE DATABASE> Creer la base de donnee hbtn_0d_2 si elle existe pas deja
CREATE DATABASE 
    IF NOT EXISTS hbtn_0d_2;

-- <CREATE USER> crée un nouvel utilisateur s'il n'existe pas déjà, sur le localhost
-- <IDENTIFIED BY> définit un password pour le nouvel utilisateur
CREATE USER 
    IF NOT EXISTS 'user_0d_2'@'localhost'
    IDENTIFIED BY 'user_0d_2_pwd'

GRANT ALL PRIVILEGES
    ON *.*
    TO 'user_0d_2'@'localhost';
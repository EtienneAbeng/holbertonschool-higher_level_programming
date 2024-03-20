-- <CREATE> <USER> permet de créer un nouvel utilisateur dans le localhost
-- <IDENTIFIED BY> permet de créer un mot de passe pour le nouvel <USER>
CREATE USER
    IF NOT EXISTS 'user_0d_1'@'localhost'
    IDENTIFIED BY 'user_0d_1_pwd';
    
-- <GRANT> <ALL> <PRIVILEGES> permet d'accorder tous les privilèges à un utilisateur
GRANT ALL PRIVILEGES
    ON *.* -- Accorde tous les privilèges sur toutes les bases de données et toutes les tables
    TO 'user_0d_1'@'localhost';
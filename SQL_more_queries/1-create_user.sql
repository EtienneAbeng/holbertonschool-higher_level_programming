-- <CREATE> <USER> permet de creer un nouveau utilisateur dans mon locale host
-- <IDENTIFIED BY> permet de creer un mot de password pour le nouveau <USER>
CREATE USER 
    IF NOT EXISTS 'user_0d_1'@'localhost' 
    IDENTIFIED BY 'user_0d_1_pwd';
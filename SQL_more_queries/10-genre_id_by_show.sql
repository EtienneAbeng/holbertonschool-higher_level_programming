-- Active: 1710860491090@@127.0.0.1@3306@hbtn_0d_usa
-- <SELECT> Sélectionne les titres des émissions de télévision et les identifiants de genre associés
SELECT tv_shows.title, tv_show_genres.genre_id
-- <FROM> Spécifie les tables à partir desquelles obtenir les données
FROM tv_shows
-- <JOIN> Jointure avec la table des genres pour lier les genres aux émissions de télévision
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
-- <ORDER BY> Trie les résultats par ordre croissant selon le titre de l'émission et l'identifiant de genre
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

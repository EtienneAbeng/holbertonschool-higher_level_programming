-- Active: 1710860491090@@127.0.0.1@3306@hbtn_0d_usa
-- <SELECT> Sélectionne les colonnes tv_shows.title et tv_show_genres.genre_id
-- <FROM> Spécifie la table source à partir de laquelle les données sont récupérées, ici tv_shows
-- <LEFT JOIN> Effectue une jointure externe gauche entre les tables tv_shows et tv_show_genres
-- <ON> Spécifie la condition de jointure, où tv_shows.id doit correspondre à tv_show_genres.show_id
-- <ORDER BY> Trie les résultats en fonction de tv_shows.title (en ordre croissant) et tv_show_genres.genre_id (en ordre croissant)
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;

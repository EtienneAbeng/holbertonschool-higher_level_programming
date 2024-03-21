-- <Import the database dump from hbtn_0d_tvshows.> Importe l'export de la base de données depuis hbtn_0d_tvshows.
-- <lists all shows, and all genres linked to that show from the database.> Liste toutes les émissions et tous les genres liés à cette émission dans la base de données.

SELECT tv_shows.title, tv_genres.name
FROM tv_shows  -- <FROM> Table source à partir de laquelle les données sont récupérées, ici tv_shows.
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id  -- <LEFT JOIN> Effectue une jointure externe gauche entre les tables tv_shows et tv_show_genres en utilisant tv_shows.id et tv_show_genres.show_id.
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id  -- <LEFT JOIN> Effectue une autre jointure externe gauche entre les tables tv_show_genres et tv_genres en utilisant tv_show_genres.genre_id et tv_genres.id.
ORDER BY tv_shows.title ASC, tv_genres.name ASC;  -- <ORDER BY> Ordonne les résultats par titre d'émission puis par nom de genre dans l'ordre croissant.

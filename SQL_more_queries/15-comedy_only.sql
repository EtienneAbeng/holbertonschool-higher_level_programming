-- <Import the database dump from hbtn_0d_tvshows.> Importer l'export de la base de données depuis hbtn_0d_tvshows.
-- <Lists all Comedy shows in the database hbtn_0d_tvshows.> Liste toutes les émissions de comédie dans la base de données hbtn_0d_tvshows.

SELECT tv_shows.title  -- <SELECT> Sélectionne les titres des émissions.
FROM tv_shows  -- <FROM> Table source à partir de laquelle les données sont récupérées, ici tv_shows.
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id  -- <JOIN> Effectue une jointure interne entre les tables tv_shows et tv_show_genres en utilisant tv_shows.id et tv_show_genres.show_id.
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id  -- <JOIN> Effectue une autre jointure interne entre les tables tv_show_genres et tv_genres en utilisant tv_show_genres.genre_id et tv_genres.id.
WHERE tv_genres.name = 'Comedy'  -- <WHERE> Filtre les résultats pour inclure uniquement les émissions de genre 'Comédie'.
ORDER BY tv_shows.title ASC;  -- <ORDER BY> Ordonne les résultats par titre d'émission dans l'ordre croissant.

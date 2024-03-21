-- <Import the database dump from hbtn_0d_tvshows.> Importer l'export de la base de données depuis hbtn_0d_tvshows.
-- <Lists all genres of the show Dexter.> Liste tous les genres de la série Dexter.

SELECT tv_genres.name  -- <SELECT> Sélectionne les noms des genres de la série Dexter.
FROM tv_genres  -- <FROM> Table source à partir de laquelle les données sont récupérées, ici tv_genres.
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id  -- <JOIN> Effectue une jointure interne entre les tables tv_genres et tv_show_genres en utilisant tv_genres.id et tv_show_genres.genre_id.
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id  -- <JOIN> Effectue une autre jointure interne entre les tables tv_show_genres et tv_shows en utilisant tv_show_genres.show_id et tv_shows.id.
WHERE tv_shows.title = 'Dexter'  -- <WHERE> Filtre les résultats pour inclure uniquement les enregistrements où le titre de l'émission est 'Dexter'.
ORDER BY tv_genres.name ASC;  -- <ORDER BY> Ordonne les résultats par nom de genre dans l'ordre croissant.

-- <SELECT> Sélectionne les titres des émissions de télévision et les identifiants de genre correspondants
-- <FROM> Spécifie la table source à partir de laquelle les données sont récupérées, ici tv_shows
-- <LEFT JOIN> Effectue une jointure externe gauche entre les tables tv_shows et tv_show_genres
-- <ON> Spécifie la condition de jointure, où tv_shows.id doit correspondre à tv_show_genres.show_id
-- <WHERE> Filtre les enregistrements pour inclure uniquement ceux où tv_show_genres.genre_id est NULL, ce qui signifie qu'il n'y a aucun genre lié
-- <ORDER BY> Trie les résultats en fonction de tv_shows.title (en ordre croissant) et tv_show_genres.genre_id (en ordre croissant)
SELECT tv_shows.title, tv_show_genres.genre_id  -- Sélectionne les titres des émissions de télévision et les identifiants de genre correspondants
FROM tv_shows  -- Spécifie la table source à partir de laquelle les données sont récupérées, ici tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id  -- Effectue une jointure externe gauche entre les tables tv_shows et tv_show_genres
WHERE tv_show_genres.genre_id IS NULL  -- Filtre les enregistrements pour inclure uniquement ceux où tv_show_genres.genre_id est NULL, ce qui signifie qu'il n'y a aucun genre lié
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;  -- Trie les résultats en fonction de tv_shows.title et tv_show_genres.genre_id (en ordre croissant)

-- List all shows with their genre ids
SELECT shows.title, show_genres.genre_id
FROM shows
LEFT JOIN show_genres ON shows.id = show_genres.show_id
ORDER BY shows.title ASC, show_genres.genre_id ASC;

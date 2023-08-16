-- List all shows with at least one genre linked
SELECT shows.title, show_genres.genre_id
FROM shows
JOIN show_genres ON shows.id = show_genres.show_id
ORDER BY shows.title ASC, show_genres.genre_id ASC;

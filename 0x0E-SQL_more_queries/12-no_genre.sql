-- List all shows without a genre linked
SELECT shows.title, show_genres.genre_id
FROM shows
LEFT JOIN show_genres ON shows.id = show_genres.show_id
WHERE show_genres.genre_id IS NULL
ORDER BY shows.title ASC, show_genres.genre_id ASC;

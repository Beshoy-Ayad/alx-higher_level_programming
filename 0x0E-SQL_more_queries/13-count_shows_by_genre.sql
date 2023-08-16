-- List all genres with number of shows linked
SELECT g.name AS genre, COUNT (sg.show_id) AS number_of_shows
FROM genres g
JOIN show_genres sg ON g.id = sg.genre_id
GROUP BY g.id
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;

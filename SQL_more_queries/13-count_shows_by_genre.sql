-- Lists all genres and displays number of shows linked to each
select tv_genres.name as genre, count(tv_genres.id) as number_of_shows from tv_genres INNER JOIN tv_show_genres on tv_genres.id = tv_show_genres.genre_id GROUP BY tv_show_genres.genre_id ORDER BY COUNT(tv_genres.id) DESC;

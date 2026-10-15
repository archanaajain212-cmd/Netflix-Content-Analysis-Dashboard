SELECT country,COUNT(*) AS total_movies
FROM netflix_titles_2
WHERE country IS NOT NULL AND type = 'Movie'
GROUP BY country
ORDER BY total_movies DESC
LIMIT 10;
SELECT country,COUNT(*) AS total_titles
FROM netflix_titles_2
WHERE country IS NOT NULL
GROUP BY country
ORDER BY total_titles DESC
LIMIT 10;
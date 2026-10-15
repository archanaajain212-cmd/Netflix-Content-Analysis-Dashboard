SELECT director,COUNT(*) AS total_titles
FROM netflix_titles_2
WHERE director IS NOT NULL
GROUP BY director
ORDER BY total_titles DESC
LIMIT 10;
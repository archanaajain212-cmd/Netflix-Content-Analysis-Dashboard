SELECT rating,COUNT(*) AS total_titles
FROM netflix_titles_2
WHERE rating IS NOT NULL
GROUP BY rating
ORDER BY total_titles DESC;
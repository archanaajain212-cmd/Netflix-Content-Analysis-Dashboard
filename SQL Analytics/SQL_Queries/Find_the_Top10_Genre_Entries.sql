SELECT listed_in AS genre,COUNT(*) AS total_titles
FROM netflix_titles_2
WHERE listed_in IS NOT NULL
GROUP BY listed_in
ORDER BY total_titles DESC
LIMIT 10;
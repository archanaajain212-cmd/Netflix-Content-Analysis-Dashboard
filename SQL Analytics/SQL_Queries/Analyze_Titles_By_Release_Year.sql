SELECT release_year,COUNT(*) AS total_titles
FROM netflix_titles_2
WHERE release_year IS NOT NULL
GROUP BY release_year
ORDER BY release_year DESC;
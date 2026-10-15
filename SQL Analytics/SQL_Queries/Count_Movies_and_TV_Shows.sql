SELECT type,COUNT(*) AS total_titles
FROM netflix_titles_2
GROUP BY type;
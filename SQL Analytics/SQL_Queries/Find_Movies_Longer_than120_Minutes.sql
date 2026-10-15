SELECT title,duration
FROM netflix_titles_2
WHERE type = 'Movie' AND CAST(SUBSTRING_INDEX(duration, ' ', 1) AS UNSIGNED) > 120
ORDER BY CAST(SUBSTRING_INDEX(duration, ' ', 1) AS UNSIGNED) DESC;
SELECT YEAR(STR_TO_DATE(date_added, '%M %d, %Y')) AS added_year,COUNT(*) AS total_titles
FROM netflix_titles_2
WHERE date_added IS NOT NULL
GROUP BY added_year
ORDER BY added_year;
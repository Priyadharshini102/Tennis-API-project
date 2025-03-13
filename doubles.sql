SELECT * FROM doubles.double_data;
SELECT competitor_name, `rank`, points
FROM doubles.double_data
ORDER BY `rank`;
SELECT * 
FROM doubles.double_data
ORDER BY `rank`
LIMIT 5;
SELECT c.competitor_name, `rank`
FROM doubles.double_data c
GROUP BY c.competitor_name, `rank`
HAVING COUNT(DISTINCT `rank`) = 1;
SELECT SUM(points) AS total_points
FROM doubles.double_data
WHERE country = 'Switzerland';
SELECT country, COUNT(*) AS number_of_competitors
FROM doubles.double_data
GROUP BY country;


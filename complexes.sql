SELECT * FROM complexes.complex_data;
SELECT complex_name, venue_name
FROM complexes.complex_data;
SELECT complex_name, COUNT(venue_name) AS venue_count
FROM complexes.complex_data
GROUP BY complex_name;
SELECT * 
FROM complexes.complex_data
WHERE country_name = 'spain';
SELECT venue_name, timezone
FROM complexes.complex_data;
SELECT complex_id, complex_name, COUNT(*) AS venue_count
FROM complexes.complex_data
GROUP BY complex_id, complex_name
HAVING venue_count > 1;
SELECT country_name, GROUP_CONCAT(venue_name ORDER BY venue_name) AS venues
FROM complexes.complex_data
GROUP BY country_name;
SELECT venue_id, venue_name, city_name, country_name, country_code,timezone
FROM complexes.complex_data
WHERE complex_name = 'Melbourne Park';
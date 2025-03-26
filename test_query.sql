-- This query returns the mean values for kpi_4 and kpi_6 and the number of times
-- the leaders changed in the database for all countries that start with 'S'.

WITH LeaderChanges AS (
    SELECT country, 
           COUNT(DISTINCT leader) AS leader_change_count
    FROM countries_misc_data
    WHERE country LIKE 'S%'  -- Filter for countries starting with 'S'
    GROUP BY country
)
SELECT c.country, 
       AVG(c.kpi_4) AS avg_kpi_4, 
       AVG(c.kpi_6) AS avg_kpi_6, 
       l.leader_change_count
FROM cities_kpis c
JOIN countries_misc_data m
    ON c.country = m.country
    AND c.date = m.date  -- Join on country and date only, no city
JOIN LeaderChanges l
    ON c.country = l.country
WHERE c.country LIKE 'S%'  -- Filter for countries starting with 'S'
GROUP BY c.country, l.leader_change_count
ORDER BY c.country;

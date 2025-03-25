with

finnish_cities as (

SELECT country, kpi_1, kpi_2, city
FROM cities_kpis
WHERE country is 'FI')

select * from finnish_cities
WHERE
kpi_1 > 300
AND
kpi_2 < 50000
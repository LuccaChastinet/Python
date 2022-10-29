SELECT name, customers_number FROM lawyers
WHERE customers_number  = (SELECT max(customers_number) FROM lawyers)
UNION ALL
SELECT name, customers_number FROM lawyers
WHERE customers_number  = (SELECT min(customers_number) FROM lawyers)
UNION ALL
SELECT 'Average' AS name, round(avg(customers_number),0)
FROM lawyers;
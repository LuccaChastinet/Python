WITH matching_temperatures AS (
	SELECT
		temperature,
		COUNT(temperature) AS matching_count
	FROM records
	GROUP BY temperature, mark
	ORDER BY mark
)
SELECT 
    temperature,
    matching_count AS number_of_records
FROM matching_temperatures
;
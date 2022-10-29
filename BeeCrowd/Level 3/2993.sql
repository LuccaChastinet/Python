SELECT amount as most_frequent_value
FROM value_table
GROUP BY amount -- or most_frequent_value
ORDER BY COUNT(*) DESC
LIMIT 1
;
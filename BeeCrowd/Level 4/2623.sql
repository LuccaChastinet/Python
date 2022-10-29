SELECT products.name, categories.name 
FROM products INNER JOIN categories ON (products.id_categories = categories.id) 
WHERE products.id_categories IN (1,2,3,6,9) AND products.amount > 100
ORDER BY categories.id ASC;
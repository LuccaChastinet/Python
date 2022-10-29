SELECT products.name 
FROM products, providers 
WHERE products.id_providers = providers.id 
AND amount BETWEEN 10 AND 20 
AND providers.name LIKE 'P%';
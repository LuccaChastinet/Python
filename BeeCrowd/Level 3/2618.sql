SELECT products.name, providers.name, categories.name
FROM  providers
JOIN products ON providers.id = products.id_providers
JOIN categories ON categories.id = products.id_categories
WHERE providers.name like 'Sansul SA' AND categories.name LIKE 'Imported';
SELECT name, cast((EXTRACT(DAY FROM payday))AS int)as day
FROM loan
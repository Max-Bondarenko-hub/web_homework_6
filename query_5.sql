SELECT d.name AS Discipline, p.name AS Professor
FROM professors AS p
JOIN disceplines AS d
ON p.disc_id = d.id
WHERE p.name = 'Lauren Ellis';
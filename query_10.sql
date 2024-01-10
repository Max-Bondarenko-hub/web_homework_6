SELECT s.name AS Student, d.name AS Discepline, p.name AS Professor, gn.name AS GroupName
FROM students AS s
JOIN group_names AS gn
ON s.group_id = gn.id
JOIN disceplines AS d
ON d.group_id = gn.id
JOIN professors AS p
ON p.disc_id = d.id
WHERE s.name = 'Marcia Chang'
AND p.name = 'John Williams'
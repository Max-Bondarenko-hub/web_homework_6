SELECT s.name AS Student, d.name AS Discepline, gn.name AS GroupName
FROM students AS s
JOIN group_names AS gn
ON s.group_id = gn.id
JOIN disceplines AS d
ON d.group_id = gn.id
WHERE s.name = 'William Robinson'
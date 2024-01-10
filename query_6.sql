SELECT gn.name AS GroupName, s.name AS Student
FROM group_names AS gn
JOIN students AS s
ON s.group_id = gn.id
WHERE gn.name = 'KI24'
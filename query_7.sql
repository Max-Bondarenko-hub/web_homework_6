SELECT gn.name AS GroupName, s.name AS Student, d.name AS Discepline, g.grade AS Grades
FROM group_names AS gn
JOIN students AS s
ON s.group_id = gn.id
JOIN disceplines AS d
ON d.group_id = gn.id
JOIN grades AS g
ON g.student_id = s.id
WHERE gn.name = 'AS55'
AND d.name = 'Math'
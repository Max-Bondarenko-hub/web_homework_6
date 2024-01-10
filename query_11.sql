SELECT s.name AS Student, p.name AS Professor, ROUND(AVG(g.grade)) AS AvgGrade
FROM students AS s
JOIN group_names AS gn
ON s.group_id = gn.id
JOIN disceplines AS d
ON d.group_id = gn.id
JOIN professors AS p
ON p.disc_id = d.id
JOIN grades AS g
ON g.student_id = s.id
WHERE s.name = 'Seth Chandler'
AND p.name = 'Douglas Smith'
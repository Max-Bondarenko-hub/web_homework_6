SELECT g.discipline_name AS Discipline, ROUND(AVG(g.grade)) AS AvgGrade, gr.name AS GroupName
FROM grades AS g
JOIN students AS s
ON s.id = g.student_id
JOIN group_names AS gr
ON s.group_id = gr.id
WHERE g.discipline_name = 'Math'
GROUP BY gr.name
ORDER BY AvgGrade DESC;
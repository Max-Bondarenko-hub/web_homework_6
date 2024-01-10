SELECT p.name AS Professor, d.name AS Discipline, ROUND(AVG(gr.grade)) AS AvgGrade
FROM grades AS gr
JOIN students AS s
ON s.id = gr.student_id
JOIN group_names AS gn
ON s.group_id = gn.id
JOIN disceplines AS d
ON d.group_id = gn.id
JOIN professors AS p
ON p.disc_id = d.id
GROUP BY p.name, d.name
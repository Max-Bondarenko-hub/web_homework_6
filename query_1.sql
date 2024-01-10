SELECT student_name AS Student, ROUND(AVG(grade)) AS AvgGrade
FROM grades
GROUP BY student_name
ORDER BY AvgGrade DESC
LIMIT 5;
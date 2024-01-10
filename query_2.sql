SELECT discipline_name AS Discipline, student_name AS Student, ROUND(AVG(grade)) AS AvgGrade
FROM grades
WHERE discipline_name = 'Math'
GROUP BY discipline_name, student_name
ORDER BY AvgGrade DESC
LIMIT 1;
-- return top5 students with highest average grade 
SELECT students.student, AVG(grades.grade) as avr
FROM grades
INNER JOIN students ON grades.student_id = students.id
GROUP BY grades.student_id
ORDER BY avr DESC
LIMIT 5
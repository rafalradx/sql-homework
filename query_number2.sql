-- return student with highest average grade for selected subject (id)
SELECT students.student, AVG(grades.grade) as avr
FROM grades
INNER JOIN students ON grades.student_id = students.id
WHERE grades.subject_id = 2
GROUP BY grades.student_id
ORDER BY avr DESC
LIMIT 1
-- average grade in groups for selected subject (id)
SELECT groups.group_name , AVG(grades.grade) as avr
FROM grades
INNER JOIN students ON grades.student_id = students.id
INNER JOIN groups ON students.group_id = groups.id
WHERE grades.subject_id = 8
GROUP BY groups.id
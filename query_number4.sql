-- average grade in groups for all grades
SELECT groups.group_name , AVG(grades.grade) as avr
FROM grades
INNER JOIN students ON grades.student_id = students.id
INNER JOIN groups ON students.group_id = groups.id
GROUP BY groups.id
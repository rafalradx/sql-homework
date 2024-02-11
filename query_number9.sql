-- return all subjects the selected student (by id) is attending to
SELECT DISTINCT subjects.subject_name 
FROM grades
INNER JOIN students ON grades.student_id = students.id
INNER JOIN subjects ON grades.subject_id = subjects.id
WHERE student_id = 16
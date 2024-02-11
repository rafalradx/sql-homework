-- return list of subjects for a given student (id) that are taught by selected
-- lecturer (id)
SELECT DISTINCT subjects.subject_name 
FROM grades
INNER JOIN students ON grades.student_id = students.id
INNER JOIN subjects ON grades.subject_id = subjects.id
INNER JOIN lecturers ON subjects.lecturer_id  = lecturers.id
WHERE student_id = 2 AND lecturers.id = 3
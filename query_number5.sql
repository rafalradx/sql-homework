-- Subjects taught by a selected lecturer (id)
SELECT subjects.subject_name 
FROM subjects 
INNER JOIN lecturers ON subjects.lecturer_id = lecturers.id
WHERE lecturers.id = 2
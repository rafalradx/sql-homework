-- average grade for selected student (id) given by selected (lecturer)
SELECT AVG(grade), students.student , lecturers.lecturer 
FROM grades
INNER JOIN students on grades.student_id = students.id
INNER JOIN subjects on grades.subject_id = subjects.id
INNER JOIN lecturers on subjects.lecturer_id = lecturers.id
WHERE lecturers.id  = 1 and grades.student_id = 12
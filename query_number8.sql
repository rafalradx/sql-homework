-- average grade for selected subject (subject_id 1 to 8) taught by lecturer
-- selected subject in conducted by only one lecturer
SELECT AVG(grade), subjects.subject_name, lecturers.lecturer 
FROM grades
INNER JOIN subjects on grades.subject_id = subjects.id
INNER JOIN lecturers on subjects.lecturer_id = lecturers.id
WHERE subject_id  = 6
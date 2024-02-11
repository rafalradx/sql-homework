-- all grades of students from selected group (id 1 to 3) and selected subject (id 1 to 8)
SELECT grade
FROM grades
WHERE subject_id  = 1 and student_id IN (SELECT id 
FROM students AS stud
WHERE stud.group_id = 3)
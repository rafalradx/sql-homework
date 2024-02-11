-- dispaly all students for selected group (by group_id 1 to 3)
SELECT g.group_name, stud.student 
FROM students AS stud
INNER JOIN groups AS g ON g.id = stud.group_id 
WHERE stud.group_id = 1
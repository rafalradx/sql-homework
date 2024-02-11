from sqlite3 import Error
from connect import create_connection, database
import faker
from random import randint, choice
from datetime import date, timedelta

NUMBER_STUDENTS = 40

GROUPS = ["alpha", "beta", "gamma"]
NUMBER_GROUPS = len(GROUPS)

GRADES = [2.0, 3.0, 3.5, 4.0, 4.5, 5.0]

SUBJECTS = [
    "General relativity",
    "Quantum electro-dynamics",
    "Probability Theory",
    "Introduction to Magnetic Resonance",
    "Protein Structure",
    "Nuclear Fusion",
    "Calculus",
    "Stochastic Processes",
]
NUMBER_SUBJECTS = len(SUBJECTS)

LECTURERS = [
    "prof. Richard Feynman",
    "prof. Erwin Hahn",
    "prof. Paul Dirac",
    "prof. John von Neumann",
    "prof. Paul Langevin",
]
NUMBER_LECTURERS = len(LECTURERS)

NUMBER_GRADES_PER_STUDENT = 20
NUMBER_GRADES = NUMBER_STUDENTS * NUMBER_SUBJECTS * NUMBER_GRADES_PER_STUDENT

START_DATE = "2023-09-01"
END_DATE = "2024-02-10"


def generate_fake_data(number_students) -> tuple:
    fake_students = []
    fake_data = faker.Faker()

    for _ in range(number_students):
        fake_students.append(fake_data.name())

    return fake_students


def random_date(start_date, end_date):
    start_date = date(*map(int, start_date.split("-")))
    end_date = date(*map(int, end_date.split("-")))

    delta = end_date - start_date
    random_days = randint(0, delta.days)
    random_date = start_date + timedelta(random_days)
    return str(random_date)


def prepare_data(groups, students, lecturers, subjects, start_date, end_date):
    for_groups = [(group,) for group in groups]
    for_lecturers = [(lecturer,) for lecturer in lecturers]

    for_students = [(student, randint(1, NUMBER_GROUPS)) for student in students]

    for_subjects = [(subject, randint(1, NUMBER_LECTURERS)) for subject in subjects]

    for_grades = []

    for subj_ind in range(1, NUMBER_SUBJECTS + 1):
        for stud_ind in range(1, NUMBER_STUDENTS + 1):
            for _ in range(NUMBER_GRADES_PER_STUDENT):
                for_grades.append(
                    (
                        choice(GRADES),
                        stud_ind,
                        subj_ind,
                        random_date(start_date, end_date),
                    )
                )

    return for_groups, for_lecturers, for_students, for_subjects, for_grades


if __name__ == "__main__":
    fake_students = generate_fake_data(NUMBER_STUDENTS)
    groups, lecturers, students, subjects, grades = prepare_data(
        groups=GROUPS,
        students=fake_students,
        lecturers=LECTURERS,
        subjects=SUBJECTS,
        start_date=START_DATE,
        end_date=END_DATE,
    )

    with open("grades.sql", "r") as fh:
        sql = fh.read()

    with create_connection(database) as conn:

        try:
            conn.executescript(sql)

            sql_to_groups = """INSERT INTO groups(group_name) VALUES (?)"""
            conn.executemany(sql_to_groups, groups)

            sql_to_lecturers = """INSERT INTO lecturers(lecturer) VALUES (?)"""
            conn.executemany(sql_to_lecturers, lecturers)

            sql_to_students = """INSERT INTO students(student, group_id) VALUES (?,?)"""
            conn.executemany(sql_to_students, students)

            sql_to_subjects = (
                """INSERT INTO subjects(subject_name, lecturer_id) VALUES (?,?)"""
            )
            conn.executemany(sql_to_subjects, subjects)

            sql_to_grades = """INSERT INTO grades(grade, student_id, subject_id, date_of) VALUES (?,?,?,?)"""
            conn.executemany(sql_to_grades, grades)

            conn.commit()
        except Error as err:
            print(err)

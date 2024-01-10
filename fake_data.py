from datetime import datetime
import faker
from random import randint, choice
import random
import sqlite3
from connection import create_connection

NUMBER_STUDENTS = 45
MAX_STUDENTS_AGE = 30
NUMBER_PROFESSORS = 5
GROUPS_NAME = ('KI24', 'PM33', 'AS55')
DISCIPLINES = ('Biology', 'History', 'Math', 'Psychology', 'Since')
MAX_NUMBER_GRADES = 20


def generate_fake_data(number_students, number_professors) -> tuple():
    fake_students = []
    fake_professors = []
    fake_data = faker.Faker()

    for _ in range(number_students):
        fake_students.append(fake_data.name())

    for _ in range(number_professors):
        fake_professors.append(fake_data.name())

    return fake_students, fake_professors

def prepare_data(fake_students, max_std_age, professors, groups):
    for_groups = []
    for gr in groups:
        for_groups.append((gr,))

    for_students = []
    for std in fake_students:
        for_students.append((std, randint(17, max_std_age), randint(1,3)))

    for_disceplines = []
    for dis in DISCIPLINES:
        for_disceplines.append((dis, randint(1,3)))

    for_professors = []
    rand_disc_list = random.sample(range(1, len(DISCIPLINES) + 1), k=len(DISCIPLINES))
    i = 0
    for prof in professors:
        for_professors.append((prof, rand_disc_list[i]))
        i += 1

    for_grades = []
    for std in students:
        for _ in range(1, MAX_NUMBER_GRADES):
            student_id = (students.index(std) + 1)
            for_grades.append((std, choice(DISCIPLINES), randint(1, 100), student_id))

    return for_students, for_professors, for_groups, for_disceplines, for_grades


def insert_data_to_db(students, professors, groups_names, disciplines, grades) -> None:
    
    with create_connection() as connection:

        cur = connection.cursor()

        sql_to_groups = "INSERT INTO group_names(name) VALUES (%s)"
        cur.executemany(sql_to_groups, groups_names)

        sql_to_students = "INSERT INTO students(name, age, group_id) VALUES (%s, %s, %s)"
        cur.executemany(sql_to_students, students)

        sql_to_disceplines = "INSERT INTO disceplines(name, group_id) VALUES (%s, %s)"
        cur.executemany(sql_to_disceplines, disciplines)

        sql_to_professors = "INSERT INTO professors(name, disc_id) VALUES (%s, %s)"
        cur.executemany(sql_to_professors, professors)

        sql_to_grades = "INSERT INTO grades(student_name, discipline_name, grade, student_id) VALUES (%s, %s, %s, %s)"
        cur.executemany(sql_to_grades, grades)

        connection.commit()

if __name__ == "__main__":
    students, professors = generate_fake_data(NUMBER_STUDENTS, NUMBER_PROFESSORS)
    std_prep, prof_prep, groups_prep, disc_prep, grades_prep = prepare_data(students, MAX_STUDENTS_AGE, professors, GROUPS_NAME)
    insert_data_to_db(std_prep, prof_prep, groups_prep, disc_prep, grades_prep)
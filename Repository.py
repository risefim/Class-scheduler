# The Repository
import atexit
import sqlite3

from DAO import Courses, Students, Classrooms


class Repository:
    def __init__(self):
        self._conn = sqlite3.connect('schedule.db')
        self.courses = Courses(self._conn)
        self.students = Students(self._conn)
        self.classrooms = Classrooms(self._conn)

    def close(self):
        self._conn.commit()
        self._conn.close()

    def create_tables(self):
        self._conn.executescript("""
        CREATE TABLE courses (
            id      INTEGER         PRIMARY KEY,
            course_name    TEXT     NOT NULL,
            student TEXT NOT NULL,
            number_of_students     INTEGER     NOT NULL,
            class_id    INTEGER REFERENCES classrooms(id),
            course_length INTEGER NOT NULL
        );

        CREATE TABLE students (
            grade TEXT PRIMARY KEY, 
            count INTEGER NOT NULL
        );

        CREATE TABLE classrooms (
            id INTEGER PRIMARY KEY,
            location TEXT NOT NULL,
            current_course_id INTEGER NOT NULL,
            current_course_time_left INTEGER NOT NULL
        );
    """)

    def print_all(self):
        c = self._conn.cursor()
        all_courses = c.execute("""
        SELECT * from courses
        """).fetchall()

        print('courses')
        for line in all_courses:
            print(line)

        c = self._conn.cursor()
        all_classrooms = c.execute("""
        SELECT * from classrooms
        """).fetchall()

        print('classrooms')
        for line in all_classrooms:
            print(line)

        c = self._conn.cursor()
        all_students = c.execute("""
        SELECT * from students
        """).fetchall()
        print('students')
        for line in all_students:
            print(line)


# the repository singleton
repo = Repository()
atexit.register(repo.close)

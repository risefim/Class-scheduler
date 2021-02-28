from DTO import Classroom, Course, Student


class Courses:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, course):
        self._conn.execute("""
               INSERT INTO courses (id, course_name, student, number_of_students,class_id,course_length) VALUES (?, ?, ?, ?, ?, ?)
           """, [course.id, course.course_name, course.student, course.number_of_students, course.class_id,
                 course.course_length])

    def find(self, id):
        c = self._conn.cursor()
        c.execute("""
            SELECT * FROM courses WHERE id = ?
        """, [id])

        row = c.fetchone()
        if row is None:
            return 0
        else:
            return [Course(*row)]

    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""
            SELECT id, course_name, student, number_of_students,class_id,course_length FROM courses
        """).fetchall()

        return [Course(*row) for row in all]

    def delete_course(self, id):
        c = self._conn.cursor()
        c.execute("""
                    DELETE FROM courses WHERE id= ?
                """, (id,))

    def is_Empty(self):
        c = self._conn.cursor()
        row = c.fetchone()
        if row is None:
            return 0
        else:
            return [Course(*row)]


class Students:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, student):
        self._conn.execute("""
                INSERT INTO students (grade, count) VALUES (?, ?)
        """, [student.grade, student.count])

    def updateStudents(self, grade, count):
        c = self._conn.cursor()
        c.execute("""
           UPDATE students
           SET count=(?)
           WHERE grade=(?)
        """, [count, grade])

    def find(self, grade):
        c = self._conn.cursor()
        c.execute("""
            SELECT * FROM students WHERE grade = ?
        """, [grade])

        row = c.fetchone()

        return [Student(*row)]


class Classrooms:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, classroom):
        self._conn.execute("""
            INSERT INTO classrooms (id, location, current_course_id, current_course_time_left) VALUES (?, ?, ?, ?)
        """, [classroom.id, classroom.location, classroom.current_course_id, classroom.current_course_time_left])

    def find_all(self):
        c = self._conn.cursor()
        all = c.execute("""
            SELECT id, location, current_course_time_left,current_course_time_left FROM classrooms
        """).fetchall()

        return [Classroom(*row) for row in all]

    def decreaseByOne(self, id, current_course_time_left):
        c = self._conn.cursor()
        c.execute("""
                UPDATE classrooms SET current_course_time_left = (?) WHERE id = (?)
                """, [current_course_time_left, id])

    def updateClassroom(self, id1, length, id2):
        c = self._conn.cursor()
        c.execute("""
           UPDATE classrooms
           SET current_course_id=(?), current_course_time_left=(?)
           WHERE id=(?)
        """, [id1, length, id2])

    def updateCourseId(self, courseId, id):
        c = self._conn.cursor()
        c.execute("""
           UPDATE classrooms
           SET current_course_id=(?)
           WHERE id=(?)
        """, [courseId, id])

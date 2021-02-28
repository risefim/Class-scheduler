import os

from Repository import repo


def main():
    all_classrooms = repo.classrooms.find_all()
    all_courses = repo.courses.find_all()
    it = 0
    while os.path.isfile('schedule.db') and len(all_courses) != 0:
        for classroom in all_classrooms:
            if classroom.current_course_time_left != 0:
                classroom.current_course_time_left = classroom.current_course_time_left - 1  # per kita
                repo.classrooms.decreaseByOne(classroom.id, classroom.current_course_time_left)
                if classroom.current_course_time_left != 0:
                    print('(' + str(it) + ') ' + classroom.location + ": occupied by " +
                          repo.courses.find(classroom.current_course_id)[0].course_name)

                else:
                    print('(' + str(it) + ') ' + classroom.location + ": " +
                          repo.courses.find(classroom.current_course_id)[
                              0].course_name + " is done")
                    for course in all_courses:
                        if course.id == classroom.current_course_id:
                            all_courses.remove(course)
                    repo.courses.delete_course(classroom.current_course_id)
                    classroom.current_course_id = 0
                    repo.classrooms.updateCourseId(classroom.current_course_id, classroom.id)

            if classroom.current_course_time_left == 0:
                for course in all_courses:
                    if course.class_id == classroom.id:
                        if classroom.current_course_id == 0:
                            if repo.students.find(course.student)[0].count >= course.number_of_students:
                                count = repo.students.find(course.student)[0].count - course.number_of_students
                                repo.students.updateStudents(course.student, count)
                                classroom.current_course_time_left = course.course_length
                                classroom.current_course_id = course.id
                                repo.classrooms.updateClassroom(classroom.current_course_id,
                                                                classroom.current_course_time_left,
                                                                classroom.id)
                                print('(' + str(
                                    it) + ') ' + classroom.location + ": " + course.course_name + " is schedule to start")

        repo.print_all()
        it = it + 1

    if it == 0:
        repo.print_all()


main()

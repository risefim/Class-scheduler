import os
import sys
import DTO


def main():
    if not os.path.isfile('schedule.db'):  # First time creating the database. Create the tables
        from Repository import repo
        repo.create_tables()
        config_file = open(sys.argv[1], 'r')
        for line in config_file:
            fields = line.split(',')
            if (fields[0].strip().__eq__('S')):
                student = DTO.Student(fields[1].strip(), fields[2].strip())
                repo.students.insert(student)
            elif (fields[0].strip().__eq__('R')):
                classroom = DTO.Classroom(fields[1].strip(), fields[2].strip(), 0, 0)
                repo.classrooms.insert(classroom)
            else:
                course = DTO.Course(fields[1].strip(), fields[2].strip(), fields[3].strip(), int(fields[4].strip()),
                                    int(fields[5].strip()), int(fields[6].strip()))
                repo.courses.insert(course)

        config_file.close()
        repo.print_all()


main()

#!/usr/bin/env python3


class Student:

    def __init__(self, name, number):
        self.name = name
        self.number = str(number)  # Fixes potential TypeError
        self.courses = {}

    def displayStudent(self):
        return 'Student Name: ' + self.name + '\n' + 'Student Number: ' + self.number

    def addGrade(self, course, grade):
        self.courses[course] = grade

    def displayGPA(self):
        gpa = 0.0
        try:
            for grade in self.courses.values():
                gpa += grade
            return 'GPA of student ' + self.name + ' is ' + str(gpa / len(self.courses))
        except ZeroDivisionError:
            return 'GPA of student ' + self.name + ' is 0.0'

    def displayCourses(self):
        return [course for course, grade in self.courses.items() if grade > 0.0]

if __name__ == '__main__':
    # Create first student object and add grades
    student1 = Student('John', '013454900')
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops245', 2.0)
    student1.addGrade('ops445', 3.0)

    # Create second student object and add grades
    student2 = Student('Jessica', 123456)
    student2.addGrade('ipc144', 4.0)
    student2.addGrade('cpp244', 3.5)
    student2.addGrade('cpp344', 0.0)

    # Output for student1
    print(student1.displayStudent())
    print(student1.displayGPA())
    print(student1.displayCourses())

    # Output for student2
    print(student2.displayStudent())
    print(student2.displayGPA())
    print(student2.displayCourses())

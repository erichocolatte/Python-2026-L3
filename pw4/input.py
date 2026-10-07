from domains.student import Student 
from domains.course import Course
import math


def input_student():
    print("====STUDENT INPUT====")
    students = []
    total_student = int(input('Total number of student: '))
    
    for i in range(total_student):
        name = input("Student name: ")
        student_id = int(input("Student ID: "))
        dob = input("DoB: ")
        students.append(Student(name, student_id, dob))
        
    return students

def input_course():
    print('====COURSE INPUT====')
    courses = []
    total_course = int(input('Total number of courses: '))
    
    for i in range(total_course):
        name = input("Course name: ")
        course_id = int(input("Course ID: "))
        credit = int(input('Course credits: '))
        courses.append(Course(name, course_id, credit))
        
    return courses

def input_mark(courses, students, Marks):
    print('====MARK INPUT====')
    
    course = input("Course name to mark students: ")
    for i in courses:
        if course == i.name:    
            Marks[course]={}    
            for j in students:
                mark = math.floor(float(input(f"{i.name} mark for {j.name}: ")) * 10) / 10  
                Marks[course][j.name] = mark  
            return Marks
        
    print("Not found")
    return Marks 
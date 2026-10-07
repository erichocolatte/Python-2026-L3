from domains.student import Student # importing class from domains dir/package
from domains.course import Course
import math
import csv

def input_student():
    print("====STUDENT INPUT====")
    students = []
    total_student = int(input('Total number of student: '))
    
    for i in range(total_student):
        name = input("Student name: ")
        student_id = int(input("Student ID: "))
        dob = input("DoB: ")
        students.append(Student(name, student_id, dob))
        
    with open("students.txt", "w") as txtfile:
        for i in students:
            txtfile.write(
                f"{i.name} | {i.student_id} | {i.dob}\n" # Write
                ) 

    with open("students.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        for i in students:
            writer.writerow([i.name, i.student_id, i.dob])
        
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
    
    # Update: write info to file
    with open("courses.txt", "w") as file:
        for i in courses:
            file.write(
                f"{i.name} | {i.course_id} | {i.credit}\n"
            )

    with open("courses.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        for i in courses:
            writer.writerow([i.name, i.course_id, i.credit])
    
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
            break
    else: 
        print("Not found")
        return Marks
    with open("marks.txt", "w") as file:
        for course_name in Marks:
            for student_name in Marks[course_name]:
                file.write(
                    f"{course_name} | {student_name} | {Marks[course_name][student_name]}\n"
                )

    with open("marks.csv", "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        for course_name in Marks:
            for student_name in Marks[course_name]:
                writer.writerow([course_name, student_name, Marks[course_name][student_name]])
    return Marks

def load_student():
    students = []
    
    with open("students.txt", "r") as file:
        for line in file:
            name, student_id, dob = line.strip().split("|") 
            
            students.append(
                Student(name, int(student_id), dob)
            )
    return students

def load_course():
    courses = []
    
    with open("courses.txt", "r") as file:
        for line in file:
            name, course_id, credit = line.strip().split("|")
            
            courses.append(
                Course(name, int(course_id), int(credit))
            )
    return courses

def load_mark():
    Marks = {} 
    
    with open("marks.txt", "r") as file:
        for line in file:
            course_name, student_name, mark = line.strip().split("|")
            
            if course_name not in Marks:
                Marks[course_name] = {}
                
            Marks[course_name][student_name] = float(mark)
    return Marks
        
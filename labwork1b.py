Students=[] 
Courses=[] 
Marks={} 


def input_student():
    total_student = int(input("Number of students in class: "))
    for i in range(total_student):
        Students.append((input("Student name: "), input("Student ID: "), input("DoB: ")))  
def input_course():
    total_course = int(input("Number of courses: "))
    for i in range(total_course):
        Courses.append((input("Course name: "), input("Course ID: ")))

def input_mark():
    course = input("Course name to mark students: ")
    for i in Courses:
        if course == i[0]:     
            Marks[course]={}     
            for j in Students:
                mark = int(input(f"{i[0]} mark for {j[0]}: "))  
                Marks[course][j[0]] = mark  
            return
    print("Not found")


    
def list_student():
    print("STUDENT INFO:")
    for i in Students:
        print(f"Student name: {i[0]} - Student ID: {i[1]} - Student DoB: {i[2]}")  
def list_course():
    print("COURSE INFO:")
    for i in Courses:
        print(f"Course name: {i[0]}, Course ID: {i[1]}")  
        
def student_marks():
    print("VIEWING MARKS:")
    course = input("Course name for viewing marks: ")   
    
    if course in Marks:
        for student_name in Marks[course]: 
            print(f"Student: {student_name}, Mark: {Marks[course][student_name]}")
    else:
        print("No marks found for this course")
    
input_student()
input_course()
input_mark()

list_student()
list_course()
student_marks()
import math
import numpy as np
import curses


Students=[] 
Courses=[]  
Marks={} 


def input_student():
    print('====STUDENT INPUT====')
    total_student = int(input("Number of students in class: "))
    for i in range(total_student):
        Students.append((input("Student name: "), input("Student ID: ")), input("DoB: "))
    
def input_course():
    print('====COURSE INPUT====')
    total_course = int(input("Number of courses: "))
    for i in range(total_course):
        Courses.append((input("Course name: "), input("Course ID: ")), int(input("Course credit: ")))

def input_mark():
    print('====MARK INPUT====')
    course = input("Course name to mark students: ")
    for i in Courses:
        if course == i[0]:     
            Marks[course]={}     
            for j in Students:
                mark = math.floor(float(input(f"{i[0]} mark for {j[0]}: ")) * 10) / 10 
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
        print(f"Course name: {i[0]}, Course ID: {i[1]}, Course credit: {i[2]}") 
        
def student_marks():
    print("VIEWING MARKS:")
    course = input("Course name for viewing marks: ")   
    
    if course in Marks:
        for student_name in Marks[course]:
            print(f"Student: {student_name}, Mark: {Marks[course][student_name]}")
    else:
        print("No marks found for this course")
    
def calc_gpa(student_name):

    marks = []
    credits = []
    
    for i in Courses:
        course_name = i[0] 
        credit = i[2]
        
        if course_name in Marks: 
            if student_name in Marks[course_name]: 
                marks.append(Marks[course_name][student_name]) 
                credits.append(credit) 
                
    if len(marks) == 0:
            return 0
        
    marks = np.array(marks)
    credits = np.array(credits)
    
    return np.sum(marks * credits) / np.sum(credits) 

def get_gpa(student):
    return calc_gpa(student[0])

def student_ranking_gpa():
    print("=======GPA COMPUTING=======")
    ranked = sorted(
        Students, key=get_gpa, reverse=True 
    )
    
    print("RANKED STUDENT BASE ON GPA: ")
    for i in ranked:
        gpa = calc_gpa(i[0])
        print(f"Name: {i[0]} - Student ID: {i[1]} - GPA: {gpa}")

def show_title():
    def screen(stdscr):
        height, width = stdscr.getmaxyx()

        if height < 8:
            stdscr.addstr(0, 0, "Please make the terminal window taller.")
            stdscr.refresh()
            stdscr.getch()
            return

        curses.start_color()
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)

        stdscr.clear()
        stdscr.border()

        stdscr.addstr(
            2, 5,
            "STUDENT MANAGEMENT SYSTEM",
            curses.color_pair(1) | curses.A_BOLD
        )

        stdscr.addstr(4, 5, "Practical Work 3")
        stdscr.addstr(6, 5, "Press any key to start...")

        stdscr.refresh()
        stdscr.getch()

    curses.wrapper(screen)
    
show_title()

input_student()
input_course()

for i in Courses:
    input_mark()

list_student()
list_course()
student_marks()

student_ranking_gpa()
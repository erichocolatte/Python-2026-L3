class SchoolEntity:
    def input_info(self):
        raise NotImplementedError("Subclasses must implement input_info()")

    def list_info(self):
        raise NotImplementedError("Subclasses must implement list_info()")


class Student(SchoolEntity):
    def __init__(self, name="", student_id="", dob=""):
        self.__name = name
        self.__student_id = student_id
        self.__dob = dob

    @property
    def name(self):
        return self.__name

    @property
    def student_id(self):
        return self.__student_id

    @property
    def dob(self):
        return self.__dob

    def input_info(self):
        self.__name = input("Student name: ")
        self.__student_id = input("Student ID: ")
        self.__dob = input("DoB: ")

    def list_info(self):
        print(f"Student name: {self.__name}, Student ID: {self.__student_id}, Student DoB: {self.__dob}")


class Course(SchoolEntity):
    def __init__(self, name="", course_id=""):
        self.__name = name
        self.__course_id = course_id

    @property
    def name(self):
        return self.__name

    @property
    def course_id(self):
        return self.__course_id

    def input_info(self):
        self.__name = input("Course name: ")
        self.__course_id = input("Course ID: ")

    def list_info(self):
        print(f"Course name: {self.__name}, Course ID: {self.__course_id}")


class SchoolManagement:
    def __init__(self):
        self.__students = []
        self.__courses = []
        self.__marks = {}

    def input_student(self):
        total_student = int(input("Number of students in class: "))
        for _ in range(total_student):
            student = Student()
            student.input_info()
            self.__students.append(student)

    def input_course(self):
        total_course = int(input("Number of courses: "))
        for _ in range(total_course):
            course = Course()
            course.input_info()
            self.__courses.append(course)

    def input_mark(self):
        course_name = input("Course name to mark students: ")
        found_course = None
        for course in self.__courses:
            if course.name == course_name:
                found_course = course
                break
        
        if found_course:
            self.__marks[course_name] = {}
            for student in self.__students:
                mark = int(input(f"{course_name} mark for {student.name}: "))
                self.__marks[course_name][student.name] = mark
        else:
            print("Not found")

    def list_student(self):
        print("STUDENT INFO:")
        for student in self.__students:
            student.list_info()  

    def list_course(self):
        print("COURSE INFO:")
        for course in self.__courses:
            course.list_info()  # Polymorphic call

    def student_marks(self):
        print("VIEWING MARKS:")
        course_name = input("Course name for viewing marks: ")   
        
        if course_name in self.__marks:
            for student_name, mark in self.__marks[course_name].items():
                print(f"Student: {student_name}, Mark: {mark}")
        else:
            print("No marks found for this course")


if __name__ == "__main__":
    manager = SchoolManagement()
    manager.input_student()
    manager.input_course()
    manager.input_mark()

    manager.list_student()
    manager.list_course()
    manager.student_marks()


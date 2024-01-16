from course import Course
from student import Student

def input_std():
    n = int(input("Enter the number of student: "))
    student_list = [0]*n
    for i in range(n):
        student_list[i] = Student(input(f"Enter the name of student {i+1}: "), input(f"Enter the id of student {i+1}: "), input(f"Enter the dob of student {i+1}: "))
    return student_list

def input_crs():
    n = int(input("Enter the number of course: "))
    course_list = [0]*n
    for i in range(n):
        course_list[i] = Course(input(f"Enter the name of course {i+1}: "), input(f"Enter the id of course {i+1}: "))
    return course_list

def input_marks(course_list, student_list):
    id = input("Enter the course id want to input marks: ");
    check = False
    for i in range(len(course_list)):
        if(course_list[i].get_crs_id() == id):
            check = True
            break

    if check == False: 
        print("There's no such that course id")
        return
    
    for i in range(len(student_list)):
        setattr(student_list[i], id, float(input(f"Enter the student {student_list[i].get_std_id()}'s mark: ")))
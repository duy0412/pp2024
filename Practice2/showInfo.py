from course import Course;
from student import Student;

def show_std(student_list):
    for i in range(len(student_list)):
        print(f"\nThe information of the student {i+1} is:\n {student_list[i].toString()}")
        

def show_crs(course_list):
    for i in range(len(course_list)):
        print(f"\nThe information of the course {i+1} is:\n {course_list[i].toString()} ")
        
def show_marks(course_list, student_list):
    check = False
    id = input("Enter the couse id that need to show marks of student: ")
    for i in range(len(course_list)):
        if (id == course_list[i].get_crs_id()):
            check = True
            break

    if check == False: 
        print("There's no such course")
        return
    

    try:
        print("The marks of all student is: ")
        for i in range (len(student_list)):
            print(f"\n{student_list[i].get_std_id()}\t{getattr(student_list[i], id)}")
    except:
        print("You haven't input marks for this course!")
    

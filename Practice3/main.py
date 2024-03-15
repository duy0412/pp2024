from course import Course
from student import Student
from showInfo import *
from input import *

student_list = 0
course_list = 0

while True:
    print("\n-----------------Menu-----------------")
    print("\n1. Input student list", "2. Input course list", "3. Input mark ", "4. Show student infor", "5. Show course infor", "6. Show marks of a course", "0. Exit",sep = "\n")
    choice = int(input("Your selection:"))
    if choice == 1:
        student_list = input_std();
    elif choice == 2:
        course_list = input_crs();
    elif choice == 3:
        input_marks(course_list, student_list)
    elif choice == 4:
        show_std(student_list)
    elif choice == 5:
        show_crs(course_list)
    elif choice == 6:
        show_marks(course_list, student_list)
    elif choice == 0:
        break;
    else:
        print("Wrong message!")
 

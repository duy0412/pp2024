from output import *
from input import *

student_list = []
course_list = []

while True:
    print("\n-----------------Menu-----------------")
    print("\n1. Input student list", "2. Input course list", "3. Input mark ", 
          "4. Show student infor", "5. Show course infor", "6. Show marks of a course", 
          "7. Write students'information into a file", "8. Write courses' information into a file","9. Write marks into a file",
          "10. Compress students, courses, marks files","11. Load all data from 3 files","12. Load student list from file", 
          "13. Load course list from file", "14. Load marks from file", "15. Compress pickle files",
          "16. Compress pickle files using Thread",
          "0. Exit",sep = "\n")
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
    elif choice == 7:
        writeToStudentFile(student_list)
    elif choice == 8:
        writeToCourseFile(course_list)
    elif choice == 9:
        writeToMarksFile(student_list, course_list)
    elif choice == 10:
        compressFile()
    elif choice == 11:
        loadDataFromCompressedFiles(student_list, course_list)
    elif choice == 12:
        loadStudentsFromFile(student_list)
    elif choice == 13:
        loadCoursesFromFile(course_list)
    elif choice == 14:
        loadMarksFromFile(student_list)
    elif choice == 15:
        writeStudentToPickleFile(student_list)
        writeCourseToPickleFile(course_list)
        compressPickleFiles()
    elif choice == 16:
        compressWithThread(student_list, course_list)
    elif choice == 0:
        break;
    else:
        print("Wrong message!")
 

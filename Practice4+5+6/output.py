from domains.course import Course
from domains.student import Student
import pickle
import zipfile
import threading
def show_std(student_list):
    for i in range(len(student_list)):
        print(f"The information of the student {i+1} is:\n {student_list[i].toString()}")
        

def show_crs(course_list):
    for i in range(len(course_list)):
        print(f"The information of the course {i+1} is:\n {course_list[i].toString()} ")
        
def show_marks(course_list, student_list):
    check = False
    id = input("Enter the course id that need to show the marks of the students: ")
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
            print(f"{student_list[i].get_std_id()}\t{getattr(student_list[i], id)}")
    except:
        print("You haven't input marks for this course!")
    

def writeToStudentFile(std_list):
    try:
        f = open("student_list.txt", "w")
        for i in range(len(std_list)):
            f.write(std_list[i].toString()+"\n")
        f.close()

    #Shorter way to access a file using WITH
        
        # with open("student_list.txt", "w") as f:
        #     for i in range(len(std_list)):
        #         f.write(std_list[i].toString()+"\n")

    except IOError:
        print("You haven't input students!!!")

def writeToCourseFile(crs_list):
    try:
        f = open("course_list.txt", "w")
        for i in range(len(crs_list)):
            f.write(crs_list[i].toString()+"\n")
        f.close()
    except IOError:
        print("You haven't input courses!!!")

def writeToMarksFile(std_list, crs_list):
    try:
        f = open("marks.txt", "w")
        f.write("Student ID")
        for i in range(len(crs_list)):
            f.write("\t"+crs_list[i].get_crs_id())
        for i in range(len(std_list)):
            f.write("\n")
            f.write(std_list[i].get_std_id())
            for j in range(len(crs_list)):
                if (hasattr(std_list[0], crs_list[j].get_crs_id())):
                    f.write("\t"+str(getattr(std_list[i],crs_list[j].get_crs_id())))
                else:
                    f.write("\t")
        f.close()
    except IOError:
        print("You haven't input marks or students or courses!!!")


def compressFile():
    with zipfile.ZipFile("student.dat", 'w') as f:
        try:
            f.write('student_list.txt')
            f.write('course_list.txt')
            f.write('marks.txt')
        except:
            print("Cannot compress files!!!")



def writeStudentToPickleFile(std_list):
    with open("student.pickle", "wb") as f:
        try:
            pickle.dump(std_list, f)
        except:
            print("Error with using pickle!!!")

def writeCourseToPickleFile(crs_list):
    with open("course.pickle", "wb") as f:
        try:
            pickle.dump(crs_list, f)
        except:
            print("Error with using pickle!!!")

def compressPickleFiles():
    with zipfile.ZipFile("pickle.dat", "w") as f:
        try:
            f.write("student.pickle")
            f.write("course.pickle")
        except:
            print("Cannot compress pickle files")


def compressWithThread(std_list, crs_list):
    f1 = threading.Thread(target = writeStudentToPickleFile, args = (std_list,))
    f2 = threading.Thread(target = writeCourseToPickleFile, args = (crs_list,))
    f1.start()
    f2.start()
    f1.join()
    f2.join()
    f3 = threading.Thread(target = compressPickleFiles)
    f3.start()
    f3.join()

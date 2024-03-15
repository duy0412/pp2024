from domains.course import Course
from domains.student import Student
import zipfile
import pickle

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
        try:
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
        except:
            print("You haven't input students or courses!!!")



# decompress a .dat/.zip file
def loadDataFromCompressedFiles(std_list = [], crs_list = []):
    try:
        with zipfile.ZipFile('student.dat', 'r') as file:
            loadStudentsFromFile(std_list)
            loadCoursesFromFile(crs_list)
            loadMarksFromFile(std_list)

    except:
        print("Cannot load from student.dat !!!")
    
def loadStudentsFromFile(std_list = []):
    try:
        with open('student_list.txt', 'r') as std_file:
            for line in std_file:
                name, id, dob = line.split("\t")
                dob = dob.removesuffix("\n")
                std_list += [Student(name, id, dob)]
    except:
        print("Cannot load from student_list.txt !!!")

def loadCoursesFromFile(crs_list = []):
    try:
        with open('course_list.txt', 'r') as crs_file:
                for line in crs_file:
                    name, id = line.split("\t")
                    id = id.removesuffix("\n")
                    crs_list += [Course(name, id)]
    except:
        print("Cannot load from course_list.txt")

def loadMarksFromFile(std_list):
    try:
        with open("marks.txt", "r") as mark_file:
            data = []
            for line in mark_file:
                temp = line.split("\t")
                temp.pop(0)
                temp[-1] = temp[-1].removesuffix("\n")
                data += [temp]
            for i in range(len(std_list)):
                for j in range(len(data[0])):
                    if(data[i+1][j] != ''):
                        setattr(std_list[i], data[0][j], data[i+1][j])

    except IOError:
        print("Cannot load from marks.txt !!!")


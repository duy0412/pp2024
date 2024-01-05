
def input_student():
    n = int(input("Enter the number of student: "))
    l = [0]*n;
    for i in range(n):
        l[i] = dict({})
        l[i]['name'] = input("Enter the name of student" + str(i+1) + ": ");
        l[i]['id'] = input("Enter the id of student" + str(i+1) + ": ");
        l[i]['dob'] = input("Enter the dob of student" + str(i+1) + ": ");
    return l

def input_course():
    n = int(input("Enter the number of course: "))
    c = [0]*n;
    for i in range(n):
        c[i] = {}
        c[i]['name'] = input("Enter the name of course number " + str(i+1) + ": ");
        c[i]['id'] = input("Enter the id of course number " + str(i+1) + ": ");
    return c

def input_mark(course_list, student_list):
    if len(course_list) == 0: 
        print("You haven't input the course list")
        return
    if len(student_list) == 0:
        print("You haven't input the student list")
        return
    
    id = input("Enter the course_id to input marks: ")
    name = ""

    for i in range(len(course_list)):
        if(course_list[i]['id'] == id):
            name = course_list[i]['name']
            break
    if(name == ""):
        print("There's no such that course_id")
        return
    for i in range(len(student_list)):
        student_list[i][name] = float(input("Enter "+ student_list[i]['id'] + "'s mark: "))

    
def show_marks(course_list, student_list):
    if len(course_list) == 0: 
        print("You haven't input the course list")
        return
    if len(student_list) == 0:
        print("You haven't input the student list")
        return
    
    id = input("Enter the course_id to show marks: ")
    name = ""

    for i in range(len(course_list)):
        if(course_list[i]['id'] == id):
            name = course_list[i]['name']
            break
    if(name == ""):
        print("There's no such that course_id")
        return
    if(name not in student_list[0]):
        print("You haven't input mark for this course!")
        return
    print("The student marks of this course is: ")
    for i in range(len(student_list)):
        print(student_list[i]['name'] + "("+student_list[i]['id']+")"+ ": "+ str(student_list[i][name]))

def show_students(student_list):
    if len(student_list) == 0:
        print("You haven't input the student list")
        return
    n = len(student_list)
    print("There're "+ str(n)+ " student:")
    print("student_name", "student_id", "dob", sep="\t")
    for i in range(n):
        print(student_list[i]['name'], student_list[i]['id'], student_list[i]['dob'], sep="\t")

def show_courses(course_list):
    if len(course_list) == 0: 
        print("You haven't input the course list")
        return
    n = len(course_list)
    print("There're "+ str(n)+ " courses:")
    print("course_name", "course_id", sep="\t")
    for i in range(n):
        print(course_list[i]['name'], course_list[i]['id'], sep="\t")

if __name__ == '__main__':
    student_list = []
    course_list = []
    while True:
        print("\n-----------------Menu-----------------")
        print("\n1. Input student list", "2. Input course list", "3. Input mark ", "4. Show student infor", "5. Show course infor", "6. Show marks of a course", "0. Exit",sep = "\n")
        choice = int(input("Your selection:"))
        if choice == 1:
            student_list = input_student();
        elif choice == 2:
            course_list = input_course();
        elif choice == 3:
            input_mark(course_list, student_list)
        elif choice == 4:
            show_students(student_list)
        elif choice == 5:
            show_courses(course_list)
        elif choice == 6:
            show_marks(course_list, student_list)
        elif choice == 0:
            break;
        else:
            break;

    
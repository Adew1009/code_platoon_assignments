from classes.school import School 
from classes.student import Student
from classes.staff import Staff
import csv
#This is an absolute import /  could also do .school import School


school = School('Ridgemont High', 
student_file_path= "./data/students.csv",
staff_file_path = "./data/staff.csv"
)
# print(school.name)

# alice = Student("alice", "5", "student", "21234324", "XXXXX")
# print(alice)
# bob = Staff("bob", "5", "teacher", "21234324", "XXXXX")
# print(bob)

# Intial Commit
#  all students
Student.all_students("./data/students.csv")
# print(Student.all_students_lst)

Staff.all_staff("./data/staff.csv")
# print(Staff.all_staff_lst)



# #open file
# with open("./data/staff.csv", mode="r") as csvfile:
#     #turn each row into dictionary
#     staff_data_reader = csv.DictReader(csvfile)
#     #loop through csv file row
#     for staff_data in staff_data_reader:
#       #destruct dictionary to be passed
#       a_staff = Staff(**staff_data)
#     #   print(a_staff)
# a_student = school.students[0] # just the first student in the list
# print(a_student.password)
# a_student.password = "XYWNF"
# print(a_student.password)

def display_main_menu():
main_menu_message = '''
Ridgemont High Student Interface 
--------------------------------
Welcome, Richard. Your access level is Principal
    What would you like to do?
    Options:
    1 List All Students
    2 View Individual Student <student_id>
    3 Add a Student
    4 Remove a Student <student_id>
    5 Quit
'''
def display_main_menu():
    user_main_menu_input = input(main_menu_message)
    print(main_menu_message_input)

    if user_main_menu_input == "1":
        display_all_student_menu():
    elif user_main_menu_input == "2":
        display_view_individual_student_menu()
    elif user_main_menu_input == "3":
        display_add_a_student_menu():
    elif user_main_menu_input == "4":
        display_remove_a_student_menu():
    elif user_main_menu_input == "5":
        exit()

    else:
        print("Invalid input, please type 1,2,3,4,5")
        display_main_menu()

display_main_menu()


def display_all_student_menu():
    print(school.students)

def display_view_individual_student_menu()
    name = input("Please enter the student you would like to view: ")
    student_name = Student.get_student_by_name(name)
    

def display_add_a_student_menu():
    print("Add Student")

def display_remove_a_student_menu():
    print("Remove StudentS")
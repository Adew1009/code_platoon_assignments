from classes.person import Person
import csv
#This is an absolute import

class Student(Person):

    all_students_lst = []

    #get all students from CSV and put in all students
    @classmethod
    def all_students(cls, path_to_file):
        with open(path_to_file, mode="r") as csvfile:
            #turn each row into dictionary
            student_data_reader = csv.DictReader(csvfile)
            #loop through csv file row
            for student_data in student_data_reader:
                #destruct dictionary to be passed
                a_student = Student(**student_data)
                cls.all_students_lst.append(a_student)
        return cls.all_students_lst     

    @classmethod
    def get_student_by_name(cls, name):
        for student in cls.all_students_lst:
            if name.lower() == student.name.lower():
                return student
            else:
                return none

    def __init__(self, name=None, age=None, role=None, school_id=None, password=None):
    # def __init__(self, name, age, role, school_id, password):   **
        super().__init__(name, age, role)
        self.school_id = school_id  
        self._password = password
        
    def __repr__(self):
        return f"{super().__repr__()} | School ID: {self.school_id}, Password : {self.password}"
       #uses fancy method
    
    @property
    def password(self):
        return f"Password: {self._password}"
    
    @password.setter
    def password(self, new_password):
        if len(new_password) <5:
            print("Password must be 5 characters")
        else:
            self._password = new_password
    



# alice = Student("alice", "5", "student", "21234324", "XXXXX")
# print(alice)
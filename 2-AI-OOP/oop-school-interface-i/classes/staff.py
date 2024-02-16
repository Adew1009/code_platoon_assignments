from classes.person import Person
import csv
#This is an absolute import

class Staff(Person):

    all_staff_lst = []
    STAFF_ROLES= ["principal", "teacher", "janitor"]
    
    @classmethod
    def is_valid_role(cls, role):
        if role.lower() in Staff.STAFF_ROLES:
            return True
        return False

    #get all students from CSV and put in all students
    @classmethod
    def all_staff(cls, path_to_file):
        with open(path_to_file, mode="r") as csvfile:
            #turn each row into dictionary
            staff_data_reader = csv.DictReader(csvfile)
            #loop through csv file row
            for staff_data in staff_data_reader:
                #destruct dictionary to be passed
                a_staff = Staff(**staff_data)
                cls.all_staff_lst.append(a_staff)
        return cls.all_staff_lst 

    def __init__(self, name=None, age=None, role=None, employee_id=None, password=None):
        super().__init__(name, age, role)
        self.employee_id = employee_id  
        self.password = password
        
    def __repr__(self):
        return f"{super().__repr__()} | employee ID: {self.employee_id}, Password : {self.password}"
       #uses fancy method of calling parent repr
    




class Person:

    def __init__(self, name, age, role):
        self.name = name 
        self.age = int(age)       # Handle cast error if invalid   
        self.role = role

    def __repr__(self):
        return f"Hello!! Different from repr Name: {self.name}, Age: {self.age} Role: {self.role}"
    
    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age} Role: {self.role}"
        
# alice = Person("alice", "5", "student")
# print(alice)
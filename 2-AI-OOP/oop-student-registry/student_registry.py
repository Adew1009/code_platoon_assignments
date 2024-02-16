import re
class Student:
    
    def __init__(self, name, age=13, grade="12th", subject = "General Studies"):
        self._name = name
        self._age = age
        self._grade = grade
        self._subject = subject
    
    def __str__(self):
        return f"Student 1: Name: {self._name}, Age: {self._age}, Grade: {self._grade}"
######## Come back and figure out how to do the "Student 1" part.
    
    @property
    def get_name(self):
        return self._name
    
    @get_name.setter
    def set_name(self, new_name):
        pattern = r'^[a-zA-Z]{3,}$'  # Regex pattern
        """
        ^[a-zA-Z]{3,}$
        Explanation:

        ^ asserts the start of the string.
        [a-zA-Z] matches any letter (uppercase or lowercase).
        {3,} specifies that the previous character class (any letter) must appear at least 3 times.
        $ asserts the end of the string.
        Here's a breakdown of each component:

        ^: Start of the string.
        [a-zA-Z]: Match any letter (uppercase or lowercase).
        {3,}: Match the previous character class (any letter) at least 3 times.
        $: End of the string.
        This regex ensures that the string consists only of letters (uppercase or lowercase) and is at least three characters long."""

        if isinstance(new_name, str) and re.match(pattern, new_name):
            self._name = new_name
        else:
            print("Student name must be a string that 3 characters or more and holds no spaces or special characters")
    
    @property
    def get_age(self):
        return self._age
    
    @get_age.setter
    def set_age(self, new_age):
        if isinstance(new_age, int) and 11<=new_age<=18:
            self._age = new_age
        else:
            print("Age must be a integer") 

    @property
    def get_grade(self):
        return self._grade
    
    @get_grade.setter
    def set_grade(self, new_grade):
        if len(new_grade)==3 and new_grade[0]=="9" and new_grade[1:]=="th":
            self._grade = new_grade
        elif len(new_grade)==4 and int(new_grade[:2]) in [10,11,12] and new_grade[2:] == "th":
            self._grade = new_grade
        else:
            print("Grade must be a string")
    
    def years_advanced(self):
        advanced_grade = int(self._grade[:-2])
        return f"{self._name} has advanced to the {advanced_grade}th"
    
    def subject(self):
        return f"{self._name} is studying {self._subject}"

    

andrew = Student("Andrew", 14, "12th")
dave = Student("Dave", 18, "11th")
# print(andrew.get_age)
# print(andrew.get_grade)
# print(andrew.get_name)

# dave.set_age = 14
dave.set_grade = "12th"
dave.set_name = "David"
print(dave.get_age)
print(dave.years_advanced())
print(dave.subject())
print(dave.get_grade)
print(dave.get_name)
    

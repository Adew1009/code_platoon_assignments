class User:

    def __init__(self, first_name, last_name, email_address, drivers_licence_num, id):
        self.first_name = first_name.lower()
        self.last_name = last_name.lower()
        self.email_address = email_address.lower()
        self.drivers_licence_num = drivers_licence_num
        self.id = id

    def __str__(self):
        return f"{self.first_name.capitalize()} {self.last_name.capitalize()} has an email of {self.email_address} and drivers license number of {self.drivers_licence_num} with id number {self.id}"

    @property
    def get_full_name(self):
        return f"Full name is equal to {self.first_name.capitalize()} {self.last_name.capitalize()}"
    
    @property
    def get_email_address(self):
        return self.email_address
    
    @get_email_address.setter
    def set_email_address(self, new_email_address):
        if isinstance(new_email_address, str):
            self.email_address = new_email_address.lower()
        else:
            print(" E-mail must be a string")


andrew = User("Andrew", "Dew", "andrew.dew@gmail.com", "118903224", 1)
emily = User("Emily", "Dew", "emilysgmail@gmail.com", "1235436436", 2)
grant = User("Grant", "Wood", "123@hotmail.com", "12489725423", 3)
print(andrew)

print(emily)
print(grant)
print(andrew.get_full_name)
andrew.set_email_address = "Adew1009@gmail.com"
print(andrew)
# your User class goes here
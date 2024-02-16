from datetime import datetime
class User:
    post_board = {}
    post_board_master = {}
    all_users = []
    user_count = 0

    @classmethod
    def publish_board(cls):
        print()
        for post in User.post_board:
            print(post + User.post_board[post])
        
    def __init__(self, first_name, last_name, email_address, drivers_licence_num):
        User.user_count +=1
        self.first_name = first_name.lower()
        self.last_name = last_name.lower()
        self.email_address = email_address.lower()
        self.drivers_licence_num = drivers_licence_num
        self.id = User.user_count
        self.screen_name = f"{self.first_name.capitalize()} {self.last_name.capitalize()}"
        User.all_users.append(self)
        

    def __str__(self):
        return f"{self.first_name.capitalize()} {self.last_name.capitalize()} has an email of {self.email_address} and drivers license number of {self.drivers_licence_num} with id number {self.id}"
    
    def __repr__(self):
        return f"||||USER DATA: {self.first_name.capitalize()} | {self.last_name.capitalize()} | {self.email_address} | {self.drivers_licence_num} | {self.id}||||" 

    def user_post(self):
        user_string = "     " + input("Enter your post: ") 
        post_name = f"{self.screen_name} at {datetime.now()} posted:"
        post = {post_name: user_string}
        User.post_board[post_name] = user_string
        User.post_board_master[post_name] = user_string
        User.publish_board()

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

def get_user_name(user_id):
    for person in User.all_users:
        if person.id == user_id:
            return person
        
    return None
andrew = User("Andrew", "Dew", "andrew.dew@gmail.com", "118903224")
emily = User("Emily", "Dew", "emilysgmail@gmail.com", "1235436436")
grant = User("Grant", "Wood", "123@hotmail.com", "12489725423")

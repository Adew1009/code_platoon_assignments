class User:
    user_count = 0
    all_users = []

    def __init__(self, first_name, last_name, email_address):
        User.user_count += 1
        self.id = User.user_count
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.screen_name = f"{self.first_name.capitalize()} {self.last_name.capitalize()}"
        User.all_users.append(self)

    def __repr__(self):
        return f"<User ID: {self.id}, Name: {self.screen_name}, Email: {self.email_address}>"

    def add_post(self, content):
        raise NotImplementedError("Subclasses must implement add_post method")

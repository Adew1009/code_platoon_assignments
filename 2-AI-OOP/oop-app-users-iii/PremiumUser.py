from User import User
from datetime import datetime

class PremiumUser(User):
    def __init__(self, first_name, last_name, email_address):
        super().__init__(first_name, last_name, email_address)
        self.posts = []

    def add_post(self, content):
        timestamp = datetime.now()
        self.posts.append((timestamp, content))
        print(f"Post added for {self.screen_name}")
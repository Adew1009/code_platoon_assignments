from User import User
from datetime import datetime

class FreeUser(User):
    max_posts = 2

    def __init__(self, first_name, last_name, email_address):
        super().__init__(first_name, last_name, email_address)
        self.posts = []

    def add_post(self, content):
        if len(self.posts) < self.max_posts:
            timestamp = datetime.now()
            self.posts.append((timestamp, content))
            print(f"Post added for {self.screen_name}")
        else:
            print(f"Cannot add more than {self.max_posts} posts for a FreeUser")

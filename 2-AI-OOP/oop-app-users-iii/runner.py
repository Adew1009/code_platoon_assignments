from FreeUser import FreeUser
from PremiumUser import PremiumUser
from datetime import datetime

# # Creating instances
free_user = FreeUser("John", "Doe", "john@example.com")
premium_user = PremiumUser("Jane", "Smith", "jane@example.com")

# # Testing add_post method
# free_user.add_post("Hello, this is my first post as a free user.")
# free_user.add_post("This is my second post as a free user.")
# free_user.add_post("This post should not be added, as the free user has reached the post limit.")

# premium_user.add_post("Hello, this is my premium post.")
# premium_user.add_post("This is another premium post.")


def create_free_user():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email address: ")
    return FreeUser(first_name, last_name, email)

def create_premium_user():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    email = input("Enter email address: ")
    return PremiumUser(first_name, last_name, email)

def create_post(user):
    post_content = input("Enter your post: ")
    user.add_post(post_content)

def display_menu():
    print("1. Create Free User")
    print("2. Create Premium User")
    print("3. Add Post")
    print("4. Quit")

def run_menu():
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            user = create_free_user()
            print(f"Free user created: {user}")
        elif choice == "2":
            user = create_premium_user()
            print(f"Premium user created: {user}")
        elif choice == "3":
            user_id = int(input("Enter user ID: "))
            user = get_user_by_id(user_id)
            if user:
                create_post(user)
            else:
                print("User not found.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def get_user_by_id(user_id):
    for user in (FreeUser.all_users + PremiumUser.all_users):
        if user.id == user_id:
            return user
    return None

if __name__ == "__main__":
    run_menu()

free_user = FreeUser("John", "Doe", "john@example.com")
premium_user = PremiumUser("Jane", "Smith", "jane@example.com")
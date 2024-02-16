from User import User
import re



def get_user_name(user_id):
    for person in User.all_users:
        if person.id == user_id:
            return person
    return None

def get_user_menu_choice():
    regex = '[1-3]'
    valid_input = False
    while not valid_input:
        print()
        print()
        print("___WELCOME TO THE NEW X___")
        print('1.  Create a post')
        print('2.  delete a post')
        print('3.  Quit')
        user_input = input('Please enter a menu option (1-3):  ')
        valid_input = bool(re.fullmatch(regex, user_input))

    return user_input

# def enter_car_id():
#     valid_input = False
#     while not valid_input:
#         user_input = int(input('Please enter a car ID: '))
#         valid_input = True #bool(user_input in CarManager.all_cars)  fix hard coded to true
#     return user_input

# def get_car_name(car_id):
#     for car in CarManager.all_cars:
#         if car._id == car_id:
#             return car
    return None

def display_menu():
    user_selection = "<>"

    while user_selection != '3':
        user_selection = get_user_menu_choice()

        match user_selection:
            case "1":
                print("*****Create a Post *****")
                valid_input = False
                while not valid_input:
                    # user_id = int(input("Enter your User ID Number: "))
                    user_id = int(input("Enter your User ID Number: "))
                    valid_input = bool(0<=user_id<=User.user_count)
                
                name = get_user_name(user_id)
                name.user_post()
                print()
            case "2":
                print('*****Delete a Post*****')
                post = input("Copy and paste the the username timestamp you wish to delete ie 'Grant Wood at 2024-02-07 22:53:28.607536 posted:' :")
                del User.post_board[post]
                User.publish_board()
            case "3":
                print("*****Goodbye*****")
                return
            
display_menu()


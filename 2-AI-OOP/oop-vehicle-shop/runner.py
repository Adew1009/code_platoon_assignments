from car_management import CarManager 
import re

def get_user_menu_choice():
    regex = '[1-7]'
    valid_input = False
    while not valid_input:
        print()
        print()
        print("___WELCOME____")
        print('1.  Add a car')
        print('2.  View all cars')
        print('3.  View total number of cars')
        print("4.  See a car's details")
        print('5.  Service a car')
        print('6.  Update mileage')
        print('7.  Quit')
        user_input = input('Please enter a menu option (1-7):  ')
        valid_input = bool(re.fullmatch(regex, user_input))

    return user_input

def enter_car_id():
    valid_input = False
    while not valid_input:
        user_input = int(input('Please enter a car ID: '))
        valid_input = True #bool(user_input in CarManager.all_cars)  fix hard coded to true
    return user_input

def get_car_name(car_id):
    for car in CarManager.all_cars:
        if car._id == car_id:
            return car
    return None

def display_menu():
    user_selection = "<>"

    while user_selection != '7':
        user_selection = get_user_menu_choice()
        print(f'The user entered option {user_selection}')

        match user_selection:
            case "1":
                print("*****Add a car*****")
                CarManager.add_car() 
                print(CarManager.all_cars)
            case "2":
                print('*****View all cars*****')
                print(CarManager.all_cars)
            case "3":
                print('*****View total number of cars*****')
                print(CarManager.total_cars)
            case "4":
                print("*****See a car's details*****" )
                car_id = enter_car_id()
                name = get_car_name(car_id)
                print(name)
            case "5":
                print('*****Service a car*****')
                car_id = enter_car_id()
                name = get_car_name(car_id)
                car_services = input("Please enter one car services")
                name.set_services = car_services
                print()
                print(f"*****New service on Car ID {car_id} are {car_services}*****")
            case "6":
                print('*****Update mileage*****')
                car_id = enter_car_id()
                name = get_car_name(car_id)
                car_mileage = int(input('Please enter new mileage: '))
                name.set_mileage = car_mileage
                print()
                print(f"*****New mileage on Car ID {car_id} is set to {car_mileage} miles*****")
            
            case "7":
                print("*****Goodbye*****")
                return
            case _:
                pass
    


display_menu()

# my_car = CarManager("Toyota", "Camry", 2021, 16543, ["Onstar", "Free Oil Change"])
# your_car = CarManager("Ford", "Focus", 2019, 24325, ["Powertrain Warranty", "Free Oil Change"])

c
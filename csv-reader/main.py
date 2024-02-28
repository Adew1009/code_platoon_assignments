

import csv

class Dog:
    def __init__(self, name, age, breed):
        self._name = name
        self._age = age
        self._breed = breed
    
    def get_age(self):
        return self._age

# Read the CSV file and create Dog instances
dogs = []
dog_list = []
with open("dogs.csv", "r") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        dog_name, dog_age, dog_breed = row
        dog_list.append((dog_name, dog_age, dog_breed))
        if dog_name == "name":
            pass
        else:   
            dogs.append(Dog(dog_name, dog_age, dog_breed))
for dog in dog_list:
    if dog[0] == "name":
        pass
    else:
        print(f"{dog[0].capitalize()} is a{dog[1]} year old{dog[2]}.")

class Cat:
    def __init__(self, name, age, breed):
        self._name = name
        self._age = age
        self._breed = breed
    
    def get_age(self):
        return self._age

cats = []
cat_list = []
with open("cats.csv", "r") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        cat_name, cat_age, cat_breed = row
        cat_list.append((cat_name, cat_age, cat_breed))
        if cat_name == "name":
            pass
        else:
            cats.append(Cat(cat_name, cat_age, cat_breed))
for cat in cat_list:
    if cat[0] == "name":
        pass
    else:
        print(f"{cat[0].capitalize()} is a{cat[1]} year old{cat[2]}.")

animal_dictionary= {}
animal_dictionary["cat"] = cat_list
animal_dictionary["dog"] = dog_list
def animal_question():
    animal = input("Enter the animal you are interested in: ")

animal_question()
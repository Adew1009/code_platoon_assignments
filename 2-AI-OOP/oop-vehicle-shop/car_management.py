import re
class CarManager:
    all_cars = []
    total_cars = 0

    def __init__(self, make, model, year, mileage, services = []):
        CarManager.total_cars += 1
        self._id = CarManager.total_cars 
        self._make = make
        self._model = model
        self._year = year
        self._mileage = mileage
        self._services = services
        CarManager.all_cars.append(self)

   

    
    def __repr__(self):
        return f"***ID {self._id} | Year {self._year} |Make {self._make} | Model {self._model} | Mileage {self._mileage}| Services {self._services}***"
        
    def __str__(self):
        return f"This {self._year} {self._make} {self._model} with the ID of {self._id} and {self._mileage} miles has had the following services {self._services}."    

   
    @classmethod
    def add_car(cls):
        input_name = input("Enter account name: ")
        input_make = input("Enter vehicle make: ")
        input_model = input("Enter vehicle model: ")
        input_year = int(input("Enter vehicle year: "))
        input_mileage = int(input("Enter vehicle mileage: "))
        input_name = CarManager(input_make, input_model, input_year, input_mileage)

    @property
    def get_mileage(self):
        return self._mileage
    
    @get_mileage.setter
    def set_mileage(self, new_mileage):
        if new_mileage > self._mileage:
            self._mileage = new_mileage
        else:
            return "Mileage cannot be lower than recorded mileage."
    
    @property
    def get_services(self):
        return self._services
    
    @get_services.setter
    def set_services(self, service_to_add):
        self._services.append(service_to_add)


def get_car_name(car_id):
    for car in CarManager.all_cars:
        if car._id == car_id:
            return car
    return None


        
my_car = CarManager("Toyota", "Camry", 2021, 16543, ["Onstar", "Free Oil Change"])
your_car = CarManager("Ford", "Focus", 2019, 24325, ["Powertrain Warranty", "Free Oil Change"])

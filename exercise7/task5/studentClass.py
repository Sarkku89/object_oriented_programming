# File:   studentClass.py
# Author: Sarianna Junnila
# Description:  The class for students

import petClass
import carClass

#  Student class definition

class Student:
    def __init__(self, first_name, last_name, has_a_pet, has_a_car):
        self.first_name = first_name
        self.last_name = last_name
        self.has_a_pet = has_a_pet
        self.has_a_car = has_a_car

    def __str__(self):
        if self.has_a_pet == True:
            return str(self.get_first_name() +  self.get_last_name())
        else:
            return str(self.get_first_name() +  self.get_last_name())

# Mutator method for the value
    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_has_a_pet(self, has_a_pet):
        self.has_a_pet = has_a_pet
    
    def set_has_a_car(self, has_a_car):
        self.has_a_car = has_a_car

# Accessor method for the value

    def get_first_name(self):
        return self.first_name + " "

    def get_last_name(self):
        return self.last_name 

    def get_has_a_pet(self, pet):
        if self.has_a_pet == True:
            return (self.get_first_name() + "has a " + petClass.Pets.get_species(pet))
        else:
            return (self.get_first_name() +"hasn't any pets.")
    
    def get_has_a_pet(self, car):
        if self.has_a_car == True:
            return (self.get_first_name() + "has a " + carClass.get_make(car) + self.carClass.get_model(car))
        else:
            return (self.get_first_name() +"hasn't a car.")







# File:   carClass.py
# Author: Sarianna Junnila
# Description:  Defining Car class. Accessor, mutators and str method updated.

# Class definition
import studentClass


class Car:
    def __init__(self, make, model, mileage, price, color, maximum_load, trunk_size, owner):
        self.make = make
        self.model = model
        self.mileage = mileage
        self.price = price
        self.color = color
        self.maximum_load = maximum_load
        self.trunk_size = trunk_size
        self.owner = owner

# Defining the str method to return the object's state

    def __str__(self):
        return str("\nCara details:\n"+"Make: " + self.get_make() 
                    + "\nModel: " + self.get_model() 
                    + "\nMileage: " + str(self.get_mileage())
                    + "\nPrice: " +  str(self.get_price())
                    + "\nColor: " + self.get_color() 
                    + "\nMaximum load limit(kg): " +  str(self.get_maximum_load())
                    + "\nTrunk height(cm): " +  str(self.get_trunk_size())
                    + "\nOwner: " + self.get_owner())

# Mutator methods

    def set_make(self, make):
        self.make = make

    def set_model(self, model):
        self.model = model

    def set_mileage(self, mileage):
        self.mileage = mileage

    def set_price(self, price):
        self.price = price

    def set_color(self, color):
        self.color = color

    def set_maximum_load(self, maximum_load):
        self.maximum_load = maximum_load

    def set_trunk_size(self, trunk_size):
        self.trunk_size = trunk_size

    def set_owner(self, owner):
        self.owner = owner

# Asseccor methods

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_mileage(self):
        return self.mileage

    def get_price(self):
        return self.price

    def get_color(self):
        return self.color

    def get_maximum_load(self):
        return self.maximum_load

    def get_trunk_size(self):
        return self.trunk_size
    
    def get_owner(self):
        return self.owner

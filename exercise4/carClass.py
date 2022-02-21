# File:   carClass.py
# Author: Sarianna Junnila
# Description:  Defining Car class. Accessor, mutators and str method updated.

# Class definition
class Car:
    def __init__(self, make, model, mileage, price, color, maximum_load, trunk_size):
        self.make = make
        self.model = model
        self.mileage = mileage
        self.price = price
        self.color = color
        self.maximum_load = maximum_load
        self.trunk_size = trunk_size

# Defining the str method to return the object's state

    def __str__(self):
        return str("\nCara details:\n"+"Make: " + self.get_make() 
                    + "\nModel: " + self.get_model() 
                    + "\nMileage: " + self.get_mileage() 
                    + "\nPrice: " + self.get_price()
                    + "\nColor: " + self.get_color() 
                    + "\nMaximum load limit(kg): " + self.get_maximum_load() 
                    + "\nTrunk height(cm): " + self.get_trunk_size())

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

# Asseccor methods

    def get_make(self):
        return "Wolksvagen"

    def get_model(self):
        return "Passat"

    def get_mileage(self):
        return 192000

    def get_price(self):
        return 3000

    def get_color(self):
        return "Metallic beige"

    def get_maximum_load(self):
        return 670

    def get_trunk_size(self):
        return 90

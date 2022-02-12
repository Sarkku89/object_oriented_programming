"""8. Create a car object. It has the following data attributes: make, model, mileage, price, 
color, maximum load limit, size of trunk. Make them private. Write accessor and 
mutator methods to change them. Add __str__ method to print the state of the car.
"""
# Class definition
class Carr:
    def __init__(self,make, model, mileage, price, color, maximum_load,trunk_size):
        self.make = make
        self.model = model
        self.mileage = mileage
        self.price = price
        self.color = color
        self.maximum_load = maximum_load
        self.trunk_size = trunk_size
    
    def __str__(self):
        return str("\nCara details:\n"+"Make: " + self.get_make() + "\nModel: " 
            + self.get_model() + "\nMileage: " + self.get_mileage() + "\nPrice: " + self.get_price()
            + "\nColor: " + self.get_color() + "\nMaximum load limit: " + self.get_maximum_load() + "\nTrunk size: " + self.get_trunk_size())

# Mutator methods 

    def set_make(self,make):
        self.make = make

    def set_model(self,model):
        self.model = model
    
    def set_mileage(self,mileage):
        self.mileage = mileage
    
    def set_price(self,price):
        self.price = price
    
    def set_color(self,color):
        self.color = color

    def set_maximum_load(self,maximum_load):
        self.maximum_load = maximum_load

    def set_trunk_size(self,trunk_size):
        self.trunk_size = trunk_size

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


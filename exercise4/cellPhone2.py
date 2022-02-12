# File:   cellPhone2.py
# Author: Sarianna Junnila
# Description:  Takes user's input of phone's features as set them as
#   attributes and then gets the information and outputs it to the user.

# Class definition

class CellPhone:
    def __init__(self, manufact, model, retail_price, id):
        self.manufact = manufact
        self.model = model
        self.retail_price = retail_price
        self.id = id

# Str method

    def __str__(self):
        return str("\nPhone data:\n"+"Manufacturer: " + self.get_manufact() + "\nModel: " + self.get_model() + "\nRetail price: " + self.get_retail_price() + "\nID: " + self.get_id())

# Mutator methods

    def set_manufact(self, manufact):
        self.manufact = manufact

    def set_model(self, model):
        self.model = model

    def set_retail_price(self, retail_price):
        self.retail_price = retail_price

    def set_id(self, id):
        self.id = id

# Accessor methods
    def get_manufact(self):
        return self.manufact

    def get_model(self):
        return self.model

    def get_retail_price(self):
        return str(self.retail_price)

    def get_id(self):
        return str(self.id)

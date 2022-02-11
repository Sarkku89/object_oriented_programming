# File:   cellPhone.py
# Author: Sarianna Junnila
# Description:  Takes user's input of phone's features as set them as 
#   attributes and then gets the information and outputs it to the user.

# Class definition

class CellPhone:
    def __init__(self, manufact, model, retail_price):
        self.manufact = manufact
        self.model = model
        self.retail_price = retail_price

# Mutator methods

    def set_manufact(self, manufact):
        self.manufact = manufact

    def set_model(self, model):
        self.model = model

    def set_retail_price(self, retail_price):
        self.retail_price = retail_price

# Accessor methods
    def get_manufact(self):
        return self.manufact

    def get_model(self):
        return self.model

    def get_retail_price(self):
        return self.retail_price
        

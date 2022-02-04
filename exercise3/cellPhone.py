# File:   cellPhone.py
# Author: Sarianna Junnila
# Description:  Takes user's input of phone's features as set them as 
#   attributes and then gets the information and outputs it to the user.

# Class definition

class cellPhone:
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
        
# Main function definition
   
def main():
    my_cell_phone = cellPhone(
    manufact = input("Enter the manufacturer: "),
    model = input ("Enter the model number: "),
    retail_price = float(input("Enter the retail price:")))

    print("Here is the data that you provided:")
    print("Manufacturer:", my_cell_phone.get_manufact())
    print("Model:", my_cell_phone.get_model())
    print("Retail price:", my_cell_phone.get_retail_price())

main()
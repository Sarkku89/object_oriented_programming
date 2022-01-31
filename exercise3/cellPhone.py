# File:         cellPhone.py
# Author: Sarianna Junnila
# Description:  

"""Design first using pseudocode, then code this: Create a CellPhone Class. Write a
program for a class that represents a cell phone. The data attributes are manufact
(Manufacter), model (Model) and retail_price (Retail price). The class will also have the
following methods:
• __init__
• set manufact
• set model
• set retail price
• get manufact
• get model
• get retail price
Test your CellPhone Class by writing a main function that creates the needed objects
and prompts the user for the phone's manufacturer, model and retail price. Program
output with data that the user enter:
• Enter the manufacturer: Apple
• Enter the model number: 'iPhone7
• Enter the retail price: 500
• Here is the data that you provided :
• Manufacturer: Apple
• Model number: iPhone 7
• Retail price: 500.0"""


class cellPhone:
    def __init__(self, manufact, model, retail_price):
        self.manufact = manufact
        self.model = model
        self.retail_price = retail_price


    def set_manufact(self):
        self.manufact = input("Enter the manufacturer: ")

    def set_model(self):
        self.model = input ("Enter the model number: ")

    def set_retail_price(self):
        self.retail_price = float(input("Enter the retail price:"))


    def get_manufact(self):
        return self.manufact

    def get_model(self):
        return self.model

    def get_retail_price(self):
        return self.retail_price
        
        
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
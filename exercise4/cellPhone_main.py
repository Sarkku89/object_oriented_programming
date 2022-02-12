# File:   cellPhone_main.py
# Author: Sarianna Junnila
# Description:  Main function for the Cellphone class. 
#   Creates, gives attribute values and lists the objects.
#   The objects are also printed with their values.

# Importing the cellPhone2 module

import cellPhone2

# Definition of the main function

def main():
    phone_list = []
    id = 0
    manufacturors = ["Nokia", "Samsung", "Motorola", "Apple", "OnePlus", "Huawei"]
    models = ["3310", "Galaxy", "Moto G50", "11", "Nord", "P30 Pro"]
    retail_prices = [float(150), float(200), float(180), float(600), float(400), float(460)]
    manufact = ""
    model = ""
    retail_price = ""
    i = 0

# Definition of the displaying of the list

    def display_list(a_list):
        for item in (a_list):
            print(item)

# Defining the making of the list with the phone objects

    def make_list(phone):
        phone_list.append(phone)
        if len(phone_list) == 6:
            display_list(phone_list)

# A loop to give the objects the their attribute values

    while i <= 5:
        id += 1
        phone = cellPhone2.CellPhone(manufact, model, retail_price, id)     
        phone.set_id(id)
        phone.set_manufact(manufacturors[i])
        phone.set_model(models[i])
        phone.set_retail_price(retail_prices[i])
        make_list(phone)
        i += 1

# Calling the main function
main()





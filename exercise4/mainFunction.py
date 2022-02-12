# File:   mainFunction.py
# Author: Sarianna Junnila
# Description:  The main function definition for calling the CellPhone class.

import oldCellPhone

def main():
    
    my_cell_phone = oldCellPhone.CellPhone(
    manufact = input("Give me the manufacturer: "),
    model = input("Give me the model: "),
    retail_price = float(input("Give me the price: ")))

    print("\nHere is the data that you provided:")
    print("Manufacturer:", my_cell_phone.get_manufact())
    print("Model:", my_cell_phone.get_model())
    print("Retail price:", my_cell_phone.get_retail_price())

main()
# Main function definition for the cellPhone class

import cellPhone2
   
def main():
    my_cell_phone = cellPhone2.CellPhone(
    manufact = input("Enter the manufacturer: "),
    model = input ("Enter the model number: "),
    retail_price = float(input("Enter the retail price:")))

    print("Here is the data that you provided:")
    print("Manufacturer:", my_cell_phone.get_manufact())
    print("Model:", my_cell_phone.get_model())
    print("Retail price:", my_cell_phone.get_retail_price())

main()
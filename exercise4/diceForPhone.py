# File:   cellPhone_main.py
# Author: Sarianna Junnila
# Description:  The program rolls a dice and according to 


# Importing the cellPhone2 and diceClass

import cellPhone2
import diceClass

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
        
        
# Defining the making of the list with the phone objects

    def make_list(phone):
        phone_list.append(phone)
        if len(phone_list) == 6:
            rollingTheDice(phone_list)
        

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

# Combining the phones to the dice values
    
def rollingTheDice(a_list):
    print("\nRolling the dice...\n")
    dice = diceClass.Dice()
    dice.roll_the_dice()
    if dice.value == 1:
        print("You got number 1! The phone you win is:\n", a_list[0])
    if dice.value == 2:
        print("You got number 2! The phone you win is:\n", a_list[1])
    if dice.value == 3:
        print("You got number 3! The phone you win is:\n", a_list[2])
    if dice.value == 4:
        print("You got number 4! The phone you win is:\n", a_list[3])
    if dice.value == 5:
        print("You got number 5! The phone you win is:\n", a_list[4])
    if dice.value == 6:
        print("You got number 6! The phone you win is:\n", a_list[5])
    
    


# Calling the main function
main()





# File:   flowershopMain.py
# Author: Sarianna Junnila
# Description: Printing flower shops and flowers' details

import plantClass

# Defining the main function

def main():

    # Creating the rose, flower and flowershop instances

    rose1 = plantClass.Roses("Rosa chinensis", 150, "China rose", "pink", 26, True)
    rose2 = plantClass.Roses("Rosa multiflora", 200, "Baby rose", "white", 16, True)
    rose3 = plantClass.Roses("Rosa ilo", 250, "Park rose", "red", 22, False)
    flower1 = plantClass.PlantWithFlowers("Tulipa saxatilis", 25, "Lilac Wonder tulip", "lilac")
    flower2 = plantClass.PlantWithFlowers("Dianthus caryophyllus", 80, "Clove pink", "Pink")
    flower3 = plantClass.PlantWithFlowers("Viola x wittrockiana", 20, "Garden pansy", "multicolor")

    selection_list = [rose1.get_common_name(), rose2.get_common_name(), 
                        rose3.get_common_name(), flower1.get_common_name(), 
                        flower2.get_common_name(), flower3.get_common_name()]

    my_flowershop = plantClass.FlowerShop("All Flower", "Rose Avenue 31", "+123456789", selection_list)


    print("\n")
    print(my_flowershop)
    print(my_flowershop.get_selection(selection_list))
    print(rose1)
    print(rose3)
    print(flower1)


# Calling the main function

main()
# File:  shoeMain.py
# Author: Sarianna Junnila
# Description:  Main function for Shoes

import shoeClass

def main():
    shoe_dict = {}
    id = 1
    my_sneakers = shoeClass.Sneaker(38, "synthetic", "black", True, 49.99, "Nike", 2, "low ankle", "Running shoes" )
    my_heels = shoeClass.Heels(37, "Synthetic leather", "red", False, 76.50 , "Clarks", 10)
    my_hikingboots = shoeClass.HikingBoots(45, "Leather", "Brown", True, 50.00 , "Goretex", False, True)
    my_shoes = shoeClass.Shoes(39, "Textile", "Green", True, 34.60, "Basic")
    my_skiboots = shoeClass.SkiBoots(45, "Thermoplastic polyurethanes", "Grey", False, 140.0, "Atomic", "Downhill skiing","GripWalk", "Downhill Skis")
    my_skates = shoeClass.Skates(36, "Leather", "White", True, 65.40, "Bolero", "Skating", True, False, 24.5, 1.5)

    shoe_list = [my_sneakers, my_heels, my_hikingboots, my_shoes, my_skates, my_skiboots]

    while id <= 5:
        for i in shoe_list:
            shoe_dict[id] = i
            id += 1

    for key in shoe_dict:
        print(shoe_dict[key])
        print("\n")

main()
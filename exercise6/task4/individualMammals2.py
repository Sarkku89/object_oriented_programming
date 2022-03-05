# File:  individualMammals2.py
# Author: Sarianna Junnila
# Description:  Main function to create and print different mammals.

import mammalObject3

# Main function definition

def main():
    print("\n")

    # Creating Cats objects
    my_cat = mammalObject3.Cats("Cat", "Einari Halla", "Black", "Kitty", "Meoww", "raw food")
    print(my_cat)
    my_cat2 = mammalObject3.Cats("Cat", "Vilja Kilpi", "White", "Snowball", "Meoww", "chicken")
    print(my_cat2)
    print("\n")

    # Creating Dogs objects
    my_dog = mammalObject3.Dogs("Dog", "Kerttu Rauta", "Black and tan ", "Blackie", "Wuff", "kibble")
    print(my_dog)
    my_dog2 = mammalObject3.Dogs("Dog", "Tenho Pirtti", "Brown ", "Jack", "Wuff", "home meals")
    print(my_dog2)
    print("\n")

    # Creating Giraffes object
    my_giraffe = mammalObject3.Giraffes("Giraffe", "diurnal", "Africa", 500, 1200)
    print(my_giraffe)

    # Creating Bears object
    my_bear = mammalObject3.Bears("Brown Bear", "crepuscular", "Eurasia and Northern America", 135, 300)
    print(my_bear)
    print("\n")

# Calling the main function
main()
# File:  individualMammals.py
# Author: Sarianna Junnila
# Description:  Main function definition to create objects and print them.

import mammalObject2

# Main function definition

def main():
    print("\n")

    # Creating Cats objects
    my_cat = mammalObject2.Cats("Meoww", "raw food", "Einari Halla", "Cat", "Kitty")
    print(my_cat)
    my_cat2 = mammalObject2.Cats("Meoww", "chicken", "Vilja Kilpi", "Cat", "Snowball")
    print(my_cat2)

    # Creating Dogs objects
    my_dog = mammalObject2.Dogs("Wuff", "kibble", "Kerttu Rauta", "Dog", "Blackie")
    print(my_dog)
    my_dog2 = mammalObject2.Dogs("Wuff", "home meals", "Tenho Pirtti", "Dog", "Jack")
    print(my_dog2)
    print("\n")

# Calling the main function
main()
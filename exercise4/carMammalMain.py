# File:   cellPhone_main.py
# Author: Sarianna Junnila
# Description:  The program rolls a dice and according to the result 
#   picks the correct animal and checks, if it can be fit into the car.


# Importing the cellPhone2 and diceClass

import carClass
import mammalObject
import diceClass

# Definition of the main function

def animal():
    animal_list = []
    attributes_list = []
    speciess = ["Dog", "Cat", "Horse", "Guinea Pig", "Giraffe", "Donkey"]
    names = ["Blackie", "Kitty", "Beauty", "Squicky", "Mr. Tall", "Geogre"]
    sizes = [60, 45, 200, 15, 480, 150]
    weights = [15, 5, 550, 1, 950, 100]
    id = 0
    species = ""
    name = ""
    size = 0
    weight = 0

    i = 0


# Defining the making of the list with the phone objects

    def make_list(animal, list_of_attributes):
        animal_list.append(animal)
        attributes_list.append(list_of_attributes)
        if len(animal_list) == 6:
            # display_list(animal_list)
            rollingTheDice(attributes_list)

# A loop to give the objects the their attribute values

    while i <= 5:
        list_of_attributes = []
        id += 1
        animal = mammalObject.Mammal(id, species, name, size, weight)
        animal.set_id(id)
        list_of_attributes.append(id)

        animal.set_species(speciess[i])
        species = animal.get_species()
        list_of_attributes.append(species)

        animal.set_name(names[i])
        name = animal.get_name()
        list_of_attributes.append(name)

        animal.set_size(sizes[i])
        size = animal.get_size()
        list_of_attributes.append(size)

        animal.set_weight(weights[i])
        weight = animal.get_weight()
        list_of_attributes.append(weight)
        make_list(animal, list_of_attributes)
        i += 1

# Combining the animals with the car by rolling the dice

def rollingTheDice(a_list):
    make = ""
    model = ""
    mileage = 0
    price = 0
    color = ""
    maximum_load = 0
    trunk_size = 0
    print("\nRolling the dice...\n")
    dice = diceClass.Dice()
    car = carClass.Car(make, model, mileage, price,
                       color, maximum_load, trunk_size)
    trunk_height = car.get_trunk_size()
    maximum_load = car.get_maximum_load()

    # The printing of the correct output
    def prints():
        if int(animal[4]) >= maximum_load:
            print(animal[1], animal[2], "weights", animal[4], "kg and too heavy for this", car.get_make(
            ), car.get_model(), "with the maximum load of", car.get_maximum_load(), "kg\n")
            if int(animal[3]) >= trunk_height:
                print("Also,", animal[1], animal[2], " too big for this as it's hight is", animal[3], "as", car.get_model(
                ), "'s trunk height is only", car.get_trunk_size(), "cm\n")
            if int(animal[3]) <= trunk_height:
                print("Your", animal[1], animal[2],
                      "fits in height in this car\n")
        if int(animal[4]) <= maximum_load:
            print("Your", animal[1], animal[2], "is not too heavy for this", car.get_make(
            ), car.get_model(),"\n")
            if int(animal[3]) >= trunk_height:
                print("But,", animal[2], "is too tall at", animal[3], "cm as", car.get_model(
                ), "'s trunk height is only", car.get_trunk_size(), "cm.\n")
            if int(animal[3]) <= trunk_height:
                print("Also,", animal[2], "fits in height in this car\n")

    dice.roll_the_dice()


# Picking the right animal according to the dice result

    if dice.value == 1:
        animal = a_list[0]
        prints()

    if dice.value == 2:
        animal = a_list[1]
        prints()

    if dice.value == 3:
        animal = a_list[2]
        prints()

    if dice.value == 4:
        animal = a_list[3]
        prints()

    if dice.value == 5:
        animal = a_list[4]
        prints()

    if dice.value == 6:
        animal = a_list[5]
        prints()


# Calling the main function
animal()


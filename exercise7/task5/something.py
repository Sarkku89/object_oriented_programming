# File:   something.py
# Author: Sarianna Junnila
# Description:  Creating instances for all the classes, 
#   then comparing if the animals fits into the students' cars

# Importing the cellPhone2 and diceClass

import carClass
import petClass
import studentClass

# Definition of the main function


def animal():
    animal_list = []
    student1 = studentClass.Student("Einari", "Virta", True, True)
    student2 = studentClass.Student("Kirsi", "Kaivo", True, True)
    student3 = studentClass.Student("Veijo", "Raita", True, True)
    pet1 = petClass.Pets("Cat", 45, 5, student1.get_first_name()+student1.get_last_name(), "Kitty")
    pet2 = petClass.Pets("Donkey", 150, 150, student2.get_first_name()+student2.get_last_name(), "George")
    pet3 = petClass.Pets("Horse", 200, 550, student3.get_first_name()+student3.get_last_name(), "Beauty")
    car1 = carClass.Car("Wolksvagen", "Passat", 192000, 3000, "Metallic beige",
                        670, 90, student1.get_first_name()+student1.get_last_name())
    car2 = carClass.Car("Volvo", "V70", 180000, 2500, "Blue", 500,
                        85, student2.get_first_name()+student2.get_last_name())
    car3 = carClass.Car("Fiat", "Punto", 80000, 2000, "Light green",
                        430, 70, student3.get_first_name()+student3.get_last_name())

    animal_list = [pet1, pet2, pet3]
    car_list = [car1, car2, car3]
    for c in car_list:

        for a in animal_list:
            if c.get_owner() == a.get_owner():
                if a.get_size() > c.get_trunk_size() or a.get_weight() > c.get_maximum_load():
                    if a.get_size() > c.get_trunk_size() and a.get_weight() > c.get_maximum_load():
                        print("Sorry,", a.get_owner()+",  pet", a.get_species(), a.get_name(
                        ), "is too heavy and too tall for this", c.get_make(), c.get_model())

                    elif a.get_size() > c.get_trunk_size():
                        print("Sorry,", a.get_owner()+", your pet", a.get_species(
                        ) , a.get_name(), "is too tall for your", c.get_make(), c.get_model())

                    elif a.get_weight() > c.get_maximum_load():
                        print("Sorry,", a.get_owner()+", your pet", a.get_species(
                        ), a.get_name(), "is too heavy for your", c.get_make(), c.get_model())

                else:
                    print(a.get_owner()+", your", a.get_species(),
                    a.get_name(), "fits in your", c.get_make(), c.get_model())


# Calling the main function
animal()

"""5. Code the relationship you just drew in the class diagram. Then check if the pet fits into
your car or do you need a truck or a trailer. Give informative output prints. See which
pet-related methods are in the Student class and think which car related methods you
need to add to the Student class. (2 points)
"""
# File:   cellPhone_main.py
# Author: Sarianna Junnila
# Description:  The program rolls a dice and according to the result 
#   picks the correct animal and checks, if it can be fit into the car.


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
    car1= carClass.Car("Wolksvagen", "Passat",192000, 3000, "Metallic beige", 670, 90, student1.get_first_name()+student1.get_last_name())
    car2 = carClass.Car("Volvo", "V70", 180000, 2500, "Blue", 500, 85, student2.get_first_name()+student1.get_last_name())
    car3 = carClass.Car("Fiat", "Punto", 80000, 2000, "Light green", 430, 70, student3.get_first_name()+student1.get_last_name())

    animal_list= [pet1, pet2, pet3]
    car_list = [car1, car2, car3]
    student_list = [student1, student2, student3]



    print("\n does", student1.get_first_name()+"'s", pet1.get_species(), "fit into his", car1.get_make())


# Calling the main function
animal()


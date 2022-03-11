# File:   studentMammalMain.py
# Author: Sarianna Junnila
# Description: 

import petClass
import studentClass

# Defining the main function

def main():

    # Creating the Mammal and student instances

    student = studentClass.Student(
        first_name = "Tamara",
        last_name = "Jones",
        has_a_pet = True)

    student2 = studentClass.Student(
        first_name="Tommy",
        last_name="Davis",
        has_a_pet = False)

    pet = petClass.Pets(student, species = "Dog", name ="Blackie")

    print("\n")
    print(student.get_has_a_pet(pet))
    print(student2.get_has_a_pet(pet))
    print(pet)


# Calling the main function

main()
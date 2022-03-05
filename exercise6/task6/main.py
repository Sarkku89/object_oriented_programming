# File:  individualMammals2.py
# Author: Sarianna Junnila
# Description:  Main function to create and print different mammals.

import classes
import mammalClass

# Main function definition

def main():
    print("\n")

    # Creating Domestic (Cats and Dogs) and Wild (Giraffe and Bear) objects
    domestic1 = mammalClass.Dogs("Dog", "owner", "Black and tan ", "Blackie", "Wuff", "kibble")
    domestic2 = mammalClass.Dogs("Dog", "owner", "Brown ", "Jack", "Wuff", "home meals")
    domestic3 = mammalClass.Cats("Cat", "owner", "Black", "Kitty", "Meoww", "raw food")
    domestic4 = mammalClass.Cats("Cat", "owner", "White", "Snowball", "Meoww", "chicken")
    wild1  = mammalClass.Giraffes("Giraffe", "diurnal", "Africa", 500, 1200)
    wild2  = mammalClass.Giraffes("Okapi", "diurnal", "Africa", 200, 200)
    wild3 = mammalClass.Bears("Brown Bear", "crepuscular", "Eurasia and Northern America", 135, 300)
    wild4 = mammalClass.Bears("Panda",  "diurnal", "Asia", 100, 150)

    # Creating Student and Teacher objects
    student1 = classes.Student("January", "April", 2022, "Python", "Ella Niemi", wild1.get_species(), domestic1.get_species(),  3235256, 4)
    student2 = classes.Student("September", "December", 2021, "Java", "Jaakko Linna", wild2.get_species(), domestic2.get_species(), 3233264, 5)
    teacher1 = classes.Teacher("January", "April", 2022, "Python", "Allan Partanen", wild3.get_species(), domestic3.get_species(),150, 6 )
    teacher2 = classes.Teacher("September", "December", 2021, "Java", "Katariina Granat", wild4.get_species(), domestic4.get_species(),116, 3)
 


    print(teacher1)
    print(teacher2)
    print("\n")
    print(student1)
    print(student2)
    print("\n")

# Calling the main function
main()

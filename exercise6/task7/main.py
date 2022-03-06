# File:  individualMammals2.py
# Author: Sarianna Junnila
# Description:  Main function to create and print different mammals.

from random import randint
import classes
import mammalClass

# Main function definition

def main():

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

    # Creating lists for objects
    teacher_list = [teacher1, teacher2]
    student_list = [student1, student2]
    domestic_list =[domestic1,domestic2, domestic4, domestic3]
    wild_list = [wild1, wild2, wild3, wild4]

    domestics1 = []
    domestics2 = []

    # Randomly picking the domestic animals and adding their species to lists
    for i in domestic_list:

        a = randint(0,len(domestic_list)-1)
        b = randint(0,len(domestic_list)-1)
        domestics1.append(str(domestic_list[a].get_species()+ " " + domestic_list[a].get_name()))
        domestics2.append(str(domestic_list[b].get_species()+ " " + domestic_list[b].get_name()))

    for k in range(0,len(student_list)):
        
        student_list[k].set_domestic(domestics1)
        teacher_list[k].set_domestic(domestics2)
    
     # Randomly picking the wild animals and adding their species to lists

    wilds1 = []
    wilds2 = []

    for i in wild_list:

        a = randint(0,len(wild_list)-1)
        b = randint(0,len(wild_list)-1)
        wilds1.append(wild_list[a].get_species())
        wilds2.append(wild_list[b].get_species())

    for k in range(0,len(student_list)):
        
        student_list[k].set_wild(wilds1)
        teacher_list[k].set_wild(wilds2)

        print('\n')
    x = 0
    while x <= 1:
        print(student_list[x])
        print('\n')
        print(teacher_list[x])
        print('\n')
        x +=1


# Calling the main function
main()

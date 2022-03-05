# File:  individualMammals2.py
# Author: Sarianna Junnila
# Description:  Main function to create and print different mammals.

from random import randint
import classes
import mammalClass

# Main function definition

def main():
    print("\n")

    # Creating Cats objects
    student1 = classes.Student("January", "April", 2022, "Python", "Ella Niemi", 3235256, 4)
    student2 = classes.Student("September", "December", 2021, "Java", "Jaakko Linna", 3233264, 5)
    #print(student1)
    #print (student2)
    #print("\n")
    teacher1 = classes.Teacher("January", "April", 2022, "Python", "Allan Partanen", 150, 6)
    teacher2 = classes.Teacher("September", "December", 2021, "Java", "Katariina Granat", 116, 3)
    #print(teacher1)
    #print (teacher2)
    #print("\n")
    

    domestic1 = mammalClass.Dogs("Dog", student1.get_name(), "Black and tan ", "Blackie", "Wuff", "kibble")
    domestic2 = mammalClass.Dogs("Dog", teacher1.get_name(), "Brown ", "Jack", "Wuff", "home meals")
    domestic3 = mammalClass.Cats("Cat", student2.get_name(), "Black", "Kitty", "Meoww", "raw food")
    domestic4 = mammalClass.Cats("Cat", teacher2.get_name(), "White", "Snowball", "Meoww", "chicken")
    wild1  = mammalClass.Giraffes("Giraffe", "diurnal", "Africa", 500, 1200, teacher1.get_name())
    wild2  = mammalClass.Giraffes("Okapi", "diurnal", "Africa", 200, 200, teacher2.get_name())
    wild3 = mammalClass.Bears("Brown Bear", "crepuscular", "Eurasia and Northern America", 135, 300, student1.get_name())
    wild4 = mammalClass.Bears("Panda",  "diurnal", "Asia", 100, 150, student2.get_name())

    teacher_list = [teacher1, teacher2]
    student_list = [student1, student2]
    domestic_list =[domestic1,domestic2, domestic4, domestic3]
    wild_list = [wild1, wild2, wild3, wild4]

    for i in teacher_list:
        x = 0
        while x < 2:
            a = randint(0,len(domestic_list)-1)
            domestic_list[a].set_owner(i.get_name())
            print (domestic_list[a])
            b = randint(0,len(wild_list)-1)
            wild_list[b].set_benefactor(i.get_name())
            print (wild_list[b])
            x +=1
        print('\n')

    for i in student_list:
        x = 0
        while x < 2:
            a = randint(0,len(domestic_list)-1)
            domestic_list[a].set_owner(i.get_name())
            print (domestic_list[a])
            b = randint(0,len(wild_list)-1)
            wild_list[b].set_benefactor(i.get_name())
            print (wild_list[b])
            x +=1
        print('\n')






    """print(domestic1)
    print(domestic2)
    print(domestic3)
    print(domestic4)
    print("\n")
    print(wild1)
    print(wild2)
    print(wild3)
    print(wild4)"""

# Calling the main function
main()

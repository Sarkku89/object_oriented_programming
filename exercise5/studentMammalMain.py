# File:   studentMammalMain.py
# Author: Sarianna Junnila
# Description: Main function creates the class intances and printing 
#   function display the information from a dictionary.

import mammalObject
import studenClass
import diceClass

# Defining a funtion which prints out the student's name and animal's details 


def printing_info(dictionary):
    for key in dictionary:
        print("Student", key, "has a", dictionary[key])

# Defining the main function


def main():
    # Creating the Mammal and student instances

    mammal = mammalObject.Mammal(id = 1, species = "Dog", name ="Blackie", size =60, weight = 15)
    student = studenClass.Student(
        first_name = "Tamara",
        last_name = "Jones",
        student_id = 1)
    print("\n")
    new_dice= diceClass.Dice()
    sum = 0
    for count in range(0,2):  
        result = new_dice.roll_dice(6)
        print("In the",count+1,"round the dice side is:", new_dice.get_value())
        sum = sum + new_dice.get_value()
    mammal.mammalLottery(sum)
    print ("\n",student,"'s total result is'", sum, ". The animal seleceter is", mammal)



# Calling the main function

main()

"""import diceClass5.Create a class called Student and use the following data attributes:
first name, last name and student id. Remember to code accessor 
and mutator methods and str-method. Store students and their pet mammal 
to dictionary (use the mammals from Exercise 4). Think, what should 
be used as the dictionary key. Code a function that prints out 
each student and their mammal’s information. 
Use informative and clear output print.
6.Let the student select his/her pet mammal by rolling 2 dices 
and using their sum to indicate a correct mammal. The higher the number, 
the heavier mammal you get as your pet. (2 points)


 mammal = mammalObject.Mammal(
        id="1",
        species="Dog",
        name="Blackie",
        size=60,
        weight=15
    )

    mammal2 = mammalObject.Mammal(
        id="2",
        species="Cat",
        name="Kitty",
        size=45,
        weight=5
    )

    student = studenClass.Student(
        first_name="Tamara",
        last_name="Jones",
        student_id=1)

    student2 = studenClass.Student(
        first_name="Tommy",
        last_name="Davis",
        student_id=2)


    # Creating a dictionary 

    dictionary = {
        student: mammal,
        student2: mammal2
    }

    # Calling the printing function

    printing_info(dictionary)"""
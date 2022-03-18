# File:  houseMain.py
# Author: Sarianna Junnila
# Description:  Defining functions for cleaning the house

# Plant class definiton

import houseClass


def clean_windows(house):
    house.set_windows("clean")
    print("Now the windows are clean!")

def mop_the_floors(house):
    house.set_floors("clean")
    print("Now the floors are clean!")

def sweep_the_surfaces(house):
    house.set_surfaces("shining")
    print("Now the surfaces are shining!")

def make_the_bed(house):
    house.set_bed("made")
    print("Now the bed is made!")

def shop(house):
    house.set_fridge("full of groceries")
    house.set_toilet_paper("full")
    print("Not the fridge is full and we have lots of toilet paper!")


def houseMain():
    my_house = houseClass.House(
        "dirty", "dirty", "unmade", "dusty", "empty", "empty")
    print("Time for spring cleaning! At the moment", my_house)
    chore_dict = {"clean the windows": clean_windows, "mop the floors": mop_the_floors,
                  "make the bed": make_the_bed, "sweep the surfaces": sweep_the_surfaces, "shop": shop}

    for key in chore_dict:
        while True:
            try:
                x = int(input("Do you want to "+key+"? Yes = 1, No = 2 "))
                if x == 1:
                    print("Excellent! Lets dot that then!\n")
                    chore_dict[key](my_house)
                    break

                elif x == 2:
                    print("Ok! Lets pass on that then...\n")
                    break

            except:
                print("Please give only either number 1 or 2!")

    print("Let see the results:\n", my_house)


houseMain()


"""Change the diagram of Task 1 so that you ask the user,  
if he/she want to do a task or no (select 1 for yes and 2 for no).
Change the code also. Use exception handling for verifying that user does 
input an integer and the input is either 1 or 2. See example from task 4 how to use a decision point 
(the diamond shaped element) in the diagram.
"""

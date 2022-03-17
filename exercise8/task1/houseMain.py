# File:  houseMain.py
# Author: Sarianna Junnila
# Description:  Defining functions for cleaning the house

# Plant class definiton

import houseClass

def clean_windows(house):
    house.set_windows("clean")
    print(house)

def mop_the_floors(house):
    house.set_floors("clean")
    print(house)

def sweep_the_surfaces(house):
    house.set_surfaces("shining")
    print(house)

def make_the_bed(house):
    house.set_bed("made")
    print(house)

def shop(house):
    house.set_fridge("full of groceries")
    house.set_toilet_paper("full")
    print(house)

def houseMain():
    my_house = houseClass.House("dirty", "dirty", "unmade", "dusty", "empty", "empty")
    print("Time for spring cleaning! At the moment", my_house)
    print("State 1:")
    clean_windows(my_house)
    print("State 2:")
    mop_the_floors(my_house)
    print("State 3:")
    sweep_the_surfaces(my_house)
    print("State 4:")
    make_the_bed(my_house)
    print("Sate 5:")
    shop(my_house)
    print("All done!")

    
houseMain()



"""code a class(House or Flat) and have the necessary data attributes, setters, getters, 
init and str method.Then make an instance of the class(in main function)and start 
cleaning.House/flat can have any numberof windows, rooms, etc. (as you wish, 
decide some reasonable amount, it does not really matter here). 
Instance can have different states like this:
•State 1: windows dirty, floors dirty, bed unmade, surfaces dusty, fridge empty and toilet paper running out.
•State 2: like state 1 but windows are washed,and bed is made.
•State 3: like state 2but floors are vacuumed, and surfaces are dusted.
•State 4: like state 3but shopping is done so the fridge is full and there is enough toilet paper.
•State 5: like state 4, but there is more than enough toilet paper.Do not overthinkor 
“over implement”this task! You need a main function where you control the state transitions (using setters). 
You need the str-method to print the state of the object (see that output prints(=str method)are informative,
and it is easy to see the state of the object). E.g. “washing the windows”is done with setter setting 
the state of the windows data attribute.
"""
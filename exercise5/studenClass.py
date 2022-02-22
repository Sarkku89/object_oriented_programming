# File:   studentClass.py
# Author: Sarianna Junnila
# Description:  The Dice claas for the dices game.

import random

# Dice class definition

class Student:
    def __init__(self, first_name, last_name, student_id):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id

    def __str__(self):
        return str(self.get_first_name()+ self.get_last_name())

# Mutator method for the value
    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_id(self, student_id):
        self.student_id = student_id

# Accessor method for the value

    def get_first_name(self):
        return self.first_name + " "

    def get_last_name(self):
        return self.last_name 

    def get_id(self):
        return str(self.student_id)

    
    def showStudent(self):
        print("Student name:", self.first_name, self.last_name)

    # Roll the dice function to determine the number given by the dice


# Dice class definition

class Dice:
    def __init__(self):
        self.value = 0

    def __str__(self):
        return str(self.get_value())

# Roll the dice function to determine the number given by the dice

    def roll_dice(self,maximum):
        self.set_value(random.randint(1, maximum))

# Mutator method for the value
    def set_value(self, value):
        self.value = value

# Accessor method for the value

    def get_value(self):
        return self.value

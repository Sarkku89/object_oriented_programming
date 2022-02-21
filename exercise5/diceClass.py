# File:   dice_class.py
# Author: Sarianna Junnila
# Description:  The class for the dice to get the 
#   phone according to the number and phone's ID.

import random

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

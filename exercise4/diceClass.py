# File:   dice_class.py
# Author: Sarianna Junnila
# Description:  The class for the dice to get the 
#   phone according to the number and phone's ID.

import random

# Dice class definition

class Dice:
    def __init__(self):
        self.value = 1

# Roll the dice function to determine the number given by the dice

    def roll_the_dice(self):
        
        if random.randint(0,6) == 0:
            self.value = 1
        elif random.randint(0,6) == 1:
            self.value = 2
        elif random.randint(0,6) == 2:
            self.value = 3
        elif random.randint(0,6) == 3:
            self.value = 4
        elif random.randint(0,6) == 4:
            self.value = 5
        else:
            self.value = 6

# Accessor method for the value

    def get_value(self):
        return self.value

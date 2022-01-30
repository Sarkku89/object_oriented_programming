# File:         dice.py
# Author: Sarianna Junnila
# Description:  

import random

# Class definition 

class Dice:
    def __init__(self):
        self.result = 1
        self.color = 'Red'
        self.flashing_light = True

    def roll_the_dice(self):
        
        if random.randint(0,6) == 0:
            self.color = "is Red"
            self.result = 1
        elif random.randint(0,6) == 1:
            self.color = "is Blue"
            self.result = 2
        elif random.randint(0,6) == 2:
            self.color = "is Yellow"
            self.result = 3
        elif random.randint(0,6) == 3:
            self.color = "is Orange"
            self.result = 4
        elif random.randint(0,6) == 4:
            self.color = "is Green"
            self.result = 5
        else:
            self.color = "is Brown"
            self.result = 6

    def is_it_flashing(self):
        
        if random.randint(0,2) == 0:
            self.flashing_light = True
        else:
            self.flashing_light = False
        
    def get_result(self):
        return self.result
    
    def get_color(self):
        return self.color

    def get_flashing_light(self):
        if self.flashing_light == True:
            return ("The lights in the dice is flashing wildy.")
        else:
            return ("The dice is not flashing.")

# Main function definition

def first_player():

    first_player = Dice()
    print("Rolling the dice...\n")
    first_player.roll_the_dice()
    first_player.is_it_flashing()
    print("The side with the number", first_player.get_result(), "is up and the background color", first_player.get_color())
    print (first_player.get_flashing_light())
    

# Calling the main function
first_player()

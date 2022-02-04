# File:         dice.py
# Author: Sarianna Junnila
# Description:  Class "Dice" which has three attributes: result, color and flashing_light. 
#   All the attributes are randomly picked. 
import random

# Class definition 

class Dice:
    def __init__(self):
        self.result = 1
        self.color = 'Red'
        self.flashing_light = True

# Generating the result and color randomly
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

# Generating the flashing light with true or false.

    def is_it_flashing(self):
        
        if random.randint(0,2) == 0:
            self.flashing_light = True
        else:
            self.flashing_light = False

# The accessor method of the result attribute

    def get_result(self):
        return self.result
    
 # The accessor method of the result attribute
    
    def get_color(self):
        return self.color


# The accessor method of the result attribute

    def get_flashing_light(self):
        if self.flashing_light == True:
            return ("The lights in the dice is flashing wildy.")
        else:
            return ("The dice is not flashing.")


# Two dice objects

def first_player():

    first_player = Dice()
    first_player.roll_the_dice()
    return first_player.get_result()
    

def second_player():
    second_player = Dice()
    second_player.roll_the_dice()
    return second_player.get_result()


def main():
    a= first_player()
    b= second_player()
    print("Rolling the dice...\n")
    print ("The First player got: ", a)
    print ("The Seconf player got: ", b)
    print ("The sum of the throws is", a + b )

main()
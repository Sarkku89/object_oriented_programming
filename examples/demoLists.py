# File:         dice.py
# Author: Sarianna Junnila
# Description:  Class "Dice" which has three attributes: value, color and flashing_light. 
#   All the attributes are randomly picked. 
import random

# Class definition 

class Dice:
    def __init__(self):
        self.value = 0
    
    def __str__(self):
        return str(self.get_value())

# Generating the value and color randomly
    def set_value(self,value):
        self.__value = value

    def roll_dice(self,  maximum):
        self.set_value(random.radint(1, maximum))
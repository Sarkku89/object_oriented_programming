# File:         coin.py
# Source:       Tony Gaddis: Starting out with Python, fourth edition
# Modified by:  Sanna Maatta & Anne Jumppanen
# Description:  Coin object and tossing

import random

# Class definition

class Coin:
    def __init__(self, sideup_attr, material):
        self.__sideup = sideup_attr
        self.__material = material


    def toss_the_coin(self):
        
        if random.randint(0,1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

# Mutatator method "setter"
    def set_material (self, material):
        self.__material = material

# Accessor method "getter"
    def get_sideup(self):
        return self.__sideup 

# Accessor method "getter"
    def get_material(self):
        return self.__material 

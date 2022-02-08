# File:         coinModified.py
# Source:       Tony Gaddis: Starting out with Python, fourth edition
# Modified by:  Sanna Maatta & Anne Jumppanen
# Modified further by: Sarianna Junnila
# Description:  Coin object and tossing. Added new options for the possible value.

import random

# Class definition

class Coin:
    def __init__(self):
        self.sideup = 'Heads'

    def toss_the_coin(self):
        
        if random.randint(0,4) == 0:
            self.sideup = 'is Heads'
        elif random.randint(0,4) == 1:
            self.sideup = 'is Tails'
        elif random.randint(0,4) == 2:
            self.sideup = 'is upright. Neither Heads or Tails.'
        elif random.randint(0,4) == 3:
            self.sideup = 'has fallen on the ground and disappeared into a rabbit hole..'
        else:
            self.sideup = 'defines gravity and is sucked into a wormhole in space.'
        
    def get_sideup(self):
        return self.sideup

# Main function definition

def main():

    my_coin = Coin()
    print("The coin is", my_coin.get_sideup())
    print("Tossing the coin...")
    my_coin.toss_the_coin()
    print("Now the coin", my_coin.get_sideup())

# Calling the main function
main()

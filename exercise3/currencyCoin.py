# File:         coinModified.py
# Source:       Tony Gaddis: Starting out with Python, fourth edition
# Modified by:  Sanna Maatta & Anne Jumppanen
# Modified further by: Sarianna Junnila
# Description:  Coin object and tossing. Added new options for the possible result.

import random

# Class definition

class Coin:
    def __init__(self):
        self.sideup = 'Heads'
        #self.currency = currency

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

    def check_the_currency(self):
        
        if random.randint(0,4) == 0:
            self.currency = 'is Euro'
        elif random.randint(0,4) == 1:
            self.currency = 'is Pound'
        elif random.randint(0,4) == 2:
            self.currency = 'is Dollar'
        elif random.randint(0,4) == 3:
            self.currency = 'is Yen'
        else:
            self.currency = 'is Rubble'

    #def set_currency(self, currency):
        #self.currency = currency

        
    def get_sideup(self):
        return self.sideup

    def get_currency (self):
        return self.currency

# Main function definition

def main():

    my_coin = Coin()
    my_coin.currency = 'Euro'

    print("The coin is", my_coin.get_sideup(), ". It's currency is", my_coin.get_currency())
    print("Tossing the coin...")
    my_coin.toss_the_coin()
    print("Now the coin", my_coin.get_sideup())
    my_coin.check_the_currency()
    print("Now the currency ", my_coin.get_currency())
    

# Calling the main function
main()

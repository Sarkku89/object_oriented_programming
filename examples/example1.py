# File:         example1.py
# Source:       Tony Gaddis: Starting out with Python, fourth edition
# Modified by:  Sanna Maatta & Anne Jumppanen
# Description:  Coin object and tossing.

import random

# The Coin class simulates a coin that
# can be flipped.

class Coin:

    # The __init__ method initializes the sideip data attribute with "Heads"
    
    def __init__(self):
        self.__sideup = 'Heads' # __ before the attribute private and it can't be changed outside the class

    # The toss method generates a random number
    # in the range of 0 through 1. If the number
    # is 0, tehn sideup is set to 'Heads'.
    # Otherwise, sideup is set to 'Tails'.

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'
    
    # The get_sideup method returns the value
    # references by sideup

    def get_sideup(self):
        return self.__sideup

# The main function 
def main():
    # Create an object from the Coin class.
    my_coin =  Coin()

    # Display the side of the coin that dacing up
    print ('This side up:', my_coin.get_sideup())

    # Toss the coin
    my_coin.toss()
    # my_coin.__sideup = 'Someting' # This won't change the sideup attribute

    # Display the side of the coin that dacing up
    print ('This side up:', my_coin.get_sideup())

# Call the main function
main()
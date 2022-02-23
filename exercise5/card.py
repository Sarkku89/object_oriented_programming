# File:   card.py
# Author: Sarianna Junnila
# Description:  The class for single card of the deck

# Defining the Card class
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        
    # Method for displaying the card

    def show_card(self):
        print (self.value, "of", self.suit)

    # The str method for the class
    def __str__(self):
        return str(str(self.value) + " of " + self.suit)

    def set_value(self, value):
        self.value = value

    def set_suit(self, suit):
        self.suit = suit

    def get_value(self):
        return self.value
    
    def get_suit(self):
        return self.suit




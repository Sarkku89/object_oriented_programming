# File:   deck.py
# Author: Sarianna Junnila
# Description:  The class for the whole deck. 
#   Methods for building, suffling and drawing card from the deck

from card import Card
import random

# Defining the Deck class

class Deck:
    def __init__(self):
        self.cards = []
        self.build_deck()
        
    # Method for building the deck

    def build_deck(self):
        for suit in ["Spades","Clubs","Hearts", "Diamonds"]:
            for value in range(1,14):
                self.cards.append(Card(suit, value))
    
    # Method for diplaying the deck

    def show_deck(self):
        for i in self.cards:
            print (i)
    
    # Methord for suffling the deck
    
    def suffle_deck(self):
        for i in range(len(self.cards)-1,0,-1):
            r = random.randint(0,i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    # Method for drawing only card
    def draw_card(self):
        the_card = random.choice(self.cards)
        Card.set_value(the_card,the_card.value)
        Card.set_suit(the_card,the_card.suit)
        return self.cards.pop()


    
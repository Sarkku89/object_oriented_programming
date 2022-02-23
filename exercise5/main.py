# File:         main.py
# Author:       Sarianna Junnila
# Description:  Deck of cards and card games. 

import card
import deck


def main():
    
    print("Let's test that a single card works...")
    
    my_card = card.Card("Hearts", 12)
    my_card.show_card()
    print(my_card)

    print("Single card testing is over.\n")

    print("Let's test that a deck of card is created...")

    my_deck = deck.Deck()
    
    my_deck.show_deck()

    print("Card deck testing is over.\n")

    print("Let's shuffle the deck.")
    my_deck.suffle_deck()

    print("Let's test that a deck of card is shuffled...")

    my_deck.show_deck()

    print("Cards should be suffled now.\n")

    print("Let's draw 2 cards and show them.")
    print("You draw:")
    card1 = my_deck.draw_card()
    card1.show_card()
    print("Your opponent draw:")
    card1 = my_deck.draw_card()
    card1.show_card()
 
    # Code your Exercise 5 taks 7 game here. """

# Defining the card game function

def highest_value_wins(cards_drawn):
    game_deck = deck.Deck()
    print("Let's shuffle the deck.\n")
    game_deck.suffle_deck()
    my_cards = []
    your_cards = []
    if cards_drawn == 4:
        print("Let's draw 3 cards each. The highest value wins.\n")
    else:
        print("Lets draw one more card each!\n")

    #Drawing the cards

    for m in range(1,cards_drawn):
        my_card = game_deck.draw_card()
        value = card.Card.get_value(my_card)
        my_cards.append(value)
        print("I drew the", my_card)
    for y in range(1,cards_drawn):
        your_card = game_deck.draw_card()
        value = card.Card.get_value(your_card)
        your_cards.append(value)
        print("You drew the", your_card)
    
    # Concluding the winner

    if max(my_cards) > max(your_cards):
        print("\nI won with the", max(my_cards),"\n")
    elif max(your_cards) > max(my_cards):
        print("\nYou won with the", max(your_cards),"\n")
    elif max(my_cards) == max(your_cards):
        print("A tie with the", max(my_cards), ". Lets draw again!\n")
        highest_value_wins(2)

#Calling the game
highest_value_wins(4)




    

# Calling the main function here, do not change...
#main()

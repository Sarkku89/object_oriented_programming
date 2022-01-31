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
    #print("Rolling the dice...\n")
    first_player.roll_the_dice()
    #first_player.is_it_flashing()
    #print("The side with the number", first_player.get_result(), "is up and the background color", first_player.get_color())
    #print (first_player.get_flashing_light())
    return first_player.get_result()
    
def second_player():

    second_player = Dice()
    #print("Rolling the dice...\n")
    second_player.roll_the_dice()
    #second_player.is_it_flashing()
    #print("The side with the number", second_player.get_result(), "is up and the background color", second_player.get_color())
    #print (second_player.get_flashing_light())
    return second_player.get_result()
    
def third_player():

    third_player = Dice()
    #print("Rolling the dice...\n")
    third_player.roll_the_dice()
    #third_player.is_it_flashing()
    #print("The side with the number", third_player.get_result(), "is up and the background color", third_player.get_color())
    #print (third_player.get_flashing_light())
    return third_player.get_result()


def play_the_game():
    first_player_roll = int(first_player())
    print ("First player rolled number", first_player_roll)
    second_player_roll = int(second_player())
    print ("Second player rolled number", second_player_roll)
    third_player_roll = int(third_player())
    print ("Third player rolled number", third_player_roll)


# The rounds with clear winners

# Third player is played out in the first round  
    if first_player_roll > second_player_roll and second_player_roll > third_player_roll:
        print ("The Third player is out of the game! First and Second player rematch!")

# Second round with First and Second player
        first_player_roll = first_player()
        print ("Second round: First player gets:", first_player_roll)
        second_player_roll = second_player()
        print ("Second round: The Second player gets:", second_player_roll)
        if first_player_roll > second_player_roll:
            print ("The First player won the game!")
        if first_player_roll == second_player_roll:
            print ("Tie! with the number:", first_player_roll, "Roll again!")
        if second_player_roll > first_player_roll:
            print ("The Second player won the game!")



# First player is played out in the first round  
    elif second_player_roll > first_player_roll and first_player_roll < third_player_roll:
        print ("The First player is out of the game! Second and Third player rematch!")

#Second round with Second and Third player
        second_player_roll = second_player()
        print ("Second round: The Second player gets:", second_player_roll)
        third_player_roll = third_player()
        print ("Second round: Third player gets:", third_player_roll)
        if second_player_roll > third_player_roll:
            print ("The Second player won the game!")
        if second_player_roll == third_player_roll:
            print ("Tie! with the number:", second_player_roll, "Roll again!")
        if third_player_roll > second_player_roll:
            print ("The Third player won the game!")



# Second player is played out in the first round
    elif first_player_roll > second_player_roll and second_player_roll < third_player_roll:
        print ("The Second player is out of the game! First and Third player rematch!")

# Second round with first and third player
        first_player_roll = first_player()
        print ("Second round: First player gets:", first_player_roll)
        third_player_roll = third_player()
        print ("Second round: Third player gets:", third_player_roll)
        if first_player_roll > third_player_roll:
            print ("The First player won the game!")
        if first_player_roll == third_player_roll:
            print ("Tie! with the number:", first_player_roll, "Roll again!")
        if third_player_roll > first_player_roll:
            print ("The Third player won the game!")
   
    elif first_player_roll == second_player_roll == third_player_roll:
        print ("All players rolled the same number! Rematch!")
        return play_the_game()

play_the_game()
# Ties in the first round:
    
""" if first_player_roll == second_player_roll:
        print ("Tie with First and Second player! They roll the dice again!")
        first_player_roll = first_player()
        second_player_roll = second_player()
        if first_player_roll > second_player_roll:
            print ("The First player won the rematch with number", first_player_roll)
        else:
            print ("The Second player won the rematch with number", second_player_roll)

    if second_player_roll == third_player_roll:
        print ("Tie with second and third player! They roll the dice again!")
        second_player_roll = second_player()
        third_player_roll = third_player()
        if second_player_roll > third_player_roll:
            print ("The second player won the rematch with number", second_player_roll)
        else:
            print ("The third player won the rematch with number", third_player_roll)

    if first_player_roll == third_player_roll:
        print ("Tie with first and third player! They roll the dice again!")
        first_player_roll = first_player()
        third_player_roll = third_player()
        if first_player_roll > third_player_roll:
            print ("The first player won the rematch with number", first_player_roll)
        else:
            print ("The third player won the rematch with number", third_player_roll)"""



        
        
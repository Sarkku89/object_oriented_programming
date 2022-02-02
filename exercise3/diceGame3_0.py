# File:         dice.py
# Author: Sarianna Junnila
# Description: A dice game with three players, one dice and two rounds. 

import random

# Class definition 

class Dice:
    def __init__(self):
        self.result = 1
        self.color = 'Red'

# Method for get the result randomly 

    def roll_the_dice(self):
        
        if random.randint(0,6) == 0:
            self.result = 1
        elif random.randint(0,6) == 1:
            self.result = 2
        elif random.randint(0,6) == 2:
            self.result = 3
        elif random.randint(0,6) == 3:
            self.result = 4
        elif random.randint(0,6) == 4:
            self.result = 5
        else:
            self.result = 6
    
# Method for getting a color for the dice randomly 

    def color_of_the_dice(self):
        if random.randint(0,1) == 0:
            self.color = "Red"
        else:
            self.color = "Blue"

# Methods for getting the result and the color of the dice

    def get_result(self):
        return self.result
    
    def get_color(self):
        return self.color



# Instances for the class (three different players)

def first_player():

    first_player = Dice()
    first_player.roll_the_dice()
    first_player.color_of_the_dice()
    dice_color = first_player.get_color()
    first_player_res = int(first_player.get_result())
    return first_player_res, dice_color

def second_player():

    second_player = Dice()
    second_player.roll_the_dice()
    second_player.color_of_the_dice()
    dice_color = second_player.get_color()
    second_player_res = int(second_player.get_result())
    return second_player_res, dice_color

    
def third_player():

    third_player = Dice()
    third_player.roll_the_dice()
    third_player.color_of_the_dice()
    dice_color = third_player.get_color()
    third_player_res = int(third_player.get_result())
    return third_player_res, dice_color




# ---- Funtion for the game play ----

def play_the_game():
    first_player_res = first_player()[0]
    second_player_res = second_player()[0]
    third_player_res = third_player()[0]
    first_color = first_player()[1]
    second_color = second_player()[1]
    third_color = third_player()[1]
    print ("\nFirst player rolled number", first_player_res, "The dice is", first_color )
    print ("Second player rolled number", second_player_res, "The dice is", second_color)
    print ("Third player rolled number", third_player_res, "The dice is", third_color, "\n")



# ----- The first rounds with clear winners -----


    # Third player is played out in the first round 
    if first_player_res > third_player_res and second_player_res > third_player_res :
        print ("The Third player is out of the game! First and Second player rematch!\n")
        first_vs_second()


    # Second player is played out in the first round 
    elif first_player_res > second_player_res and third_player_res > second_player_res:
        print ("The Second player is out of the game! First and Third player rematch!\n")
        first_vs_third()


    # First player is played out in the first round 
    elif second_player_res > first_player_res and third_player_res > first_player_res:
        print ("The First player is out of the game! Second and Third player rematch!\n")
        second_vs_third()



# ---- Different ties between players on the first round. 
#       Notice, that if two players get same number, 
#           but the number is bigger than the third player has, 
#               they got straight to second round.


    # Tie between all players
    elif second_player_res == first_player_res == third_player_res:
        if first_color == second_color == third_color:
            print ("All players rolled the same number and have the same color dice! Rematch!\n")
            play_the_game()

        elif first_color == second_color == "Blue":
            print ("All players got the same number. The players with blue dices win the round! Sorry Third player, you are out!")
            first_vs_second()

        elif first_color == third_color == "Blue":
            print ("All players got the same number. The players with blue dices win the round! Sorry Second player, you are out!")
            first_vs_third()

        elif second_color == third_color == "Blue":
            print ("All players got the same number. The players with blue dices win the round! Sorry First player, you are out!")
            second_vs_third()


    # Tie between First and Second player. 
    elif first_player_res == second_player_res:
        print ("The Third player is through to next round!\n")
        if first_color == "Blue" or second_color == "Blue":
            if first_color == "Blue" and second_color == "Red":
                print ("First player has a Blue dice and will continue to Round 2!")
            if second_color == "Blue" and first_color == "Red":
                print ("Second player has a Blue dice and will continue to Round 2!")
        else:
            print ("A tie between First and Second player. Please roll again!")
            a = first_player()[0]
            b = second_player()[0]
            while True:
                if a > b:
                    print ("Second player is played out! First and Third player go to Round 2!\n")
                    first_vs_third()
                if b > a:
                    print ("First player is played out! Second and Third player go to Round 2!\n")
                    second_vs_third()
                if a == b:
                    print ("Tie! Roll again!")
                    a = first_player()[0]
                    b = third_player()[0]


    # Tie between First and Third player
    elif first_player_res == third_player_res:
        print ("The Second player is through to next round!\n")
        if first_color == "Blue" or third_color == "Blue":
            if first_color == "Blue" and third_color == "Red":
                print ("First player has a Blue dice and will continue to Round 2!")
            if third_color == "Blue" and first_color == "Red":
                print ("Third player has a Blue dice and will continue to Round 2!")
        else:
            print ("A tie between First and Third player. Please roll again!")
            a = first_player()[0]
            b = third_player()[0]
            while True:
                if a > b:
                    print ("Third player is played out! First and Second player go to Round 2!\n")
                    first_vs_second()
                if b > a:
                    print ("First player is played out! Second and Third player go to Round 2!\n")
                    second_vs_third()
                if a == b:
                    print ("Tie! Roll again!")
                    a = first_player()[0]
                    b = third_player()[0]


    # Tie between Second and Third
    elif second_player_res == third_player_res:
        print ("The First player is through to next round!\n")
        if second_color == "Blue" or third_color == "Blue":
            if second_color == "Blue" and third_color == "Red":
                print ("Second player has a Blue dice and will continue to Round 2!")
            if third_color == "Blue" and second_color == "Red":
                print ("Third player has a Blue dice and will continue to Round 2!")
        else:
            print ("A tie between Second and Third player. Please roll again!")
            a = second_player()[0]
            b = third_player()[0]
            while True:
                if a > b:
                    print ("Third player is played out! First and Second player go to Round 2!\n")
                    first_vs_second()
                if b > a:
                    print ("Second player is played out! First and Third player go to Round 2!\n")
                    first_vs_third()
                if a == b:
                    print ("Tie! Roll again!")
                    a = second_player()[0]
                    b = third_player()[0]


# ---- Functions for Round 2 matches ----

def first_vs_third():
    a = first_player()[0]
    b = third_player()[0]
    a_name = "First player"
    b_name = "Third player"
    second_round(a,b,a_name,b_name)

def first_vs_second():
    a = first_player()[0]
    b = second_player ()[0]
    a_name = "First player"
    b_name = "Second player"
    second_round(a,b, a_name, b_name)

def second_vs_third():
    a = second_player()[0]
    b = third_player ()[0]
    a_name = "Second player"
    b_name = "Third player"
    second_round(a,b, a_name, b_name)


# ---- Function for the Round 2 ----
def second_round(a,b, a_name, b_name):
    print(a_name,"got",a)
    print(b_name,"got",b)
    if a > b:
            print ("The winner is", a_name, "\n")
    elif b > a:
            print ("The winner is", b_name, "\n")
    elif a == b:
            print ("Tie! Roll again!")
            if a_name == "First player" and b_name == "Third player":
                first_vs_third()
            elif a_name == "First player" and b_name == "Second player":
                first_vs_second()
            else:
                second_vs_third()



# --- Calling the game function --- 
play_the_game()

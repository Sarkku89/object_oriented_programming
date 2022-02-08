# File:         diceGame2_0.py
# Author: Sarianna Junnila
# Description: A dice game with three players, one dice and two rounds. 
#   In the first round two of the highest numbers will go through,
#   and if there two of the same lower number, they will roll again
#   In the Round 2, the player with higher number wins 
#   and in a tie they roll again, until one gets a bigger number.

import random

# Class definition 

class Dice:
    def __init__(self):
        self.value = 1
        self.color = 'Red'

# Method for get the value randomly 

    def roll_the_dice(self):
        
        if random.randint(0,6) == 0:
            self.value = 1
        elif random.randint(0,6) == 1:
            self.value = 2
        elif random.randint(0,6) == 2:
            self.value = 3
        elif random.randint(0,6) == 3:
            self.value = 4
        elif random.randint(0,6) == 4:
            self.value = 5
        else:
            self.value = 6

# Method for getting the value

    def get_value(self):
        return self.value
    

# ---- Instances for the class (three different players) ----

def first_player():

    first_player = Dice()
    first_player.roll_the_dice()
    return int(first_player.get_value())

def second_player():

    second_player = Dice()
    second_player.roll_the_dice()
    return int(second_player.get_value())
    
def third_player():

    third_player = Dice()
    third_player.roll_the_dice()
    return int(third_player.get_value())



# ---- Funtion for the game play ----

def play_the_game():
    first_player_res = first_player()
    second_player_res = second_player()
    third_player_res = third_player()
    print ("\nFirst player rolled number", first_player_res)
    print ("Second player rolled number", second_player_res)
    print ("Third player rolled number", third_player_res, "\n")



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


# ---- Different ties between players on the first round. ----

#       Notice, that if two players get same number, 
#       but the number is bigger than the third player got, 
#       the pleyer with bigger number go straight to second round.


    # Tie between all players
    elif second_player_res == first_player_res == third_player_res:
        print ("All players rolled the same number! Rematch!\n")
        play_the_game()


    # Tie between First and Second player. 
    elif first_player_res == second_player_res:
        print ("First and Second player had a tie! Roll again! The Third player is through to next round!\n")
        a = first_player()
        b = second_player()
        while True:
            if a > b:
                print ("Second player is played out! First and Third player go to Round 2!\n")
                first_vs_third()
                break
            if b > a:
                print ("First player is played out! Second and Third player go to Round 2!\n")
                second_vs_third()
                break
            if a == b:
                print ("Tie! Roll again!")
                a = first_player()
                b = third_player()


    # Tie between First and Third player
    elif first_player_res == third_player_res:
        print ("First and Third player had a tie! Roll again! The Second player is through to next round!\n")
        a = first_player()
        b = third_player()
        while True:
            if a > b:
                print ("Third player is played out! First and Second player go to Round 2!\n")
                first_vs_second()
                break
            if b > a:
                print ("First player is played out! Second and Third player go to Round 2!\n")
                second_vs_third()
                break
            if a == b:
                print ("Tie! Roll again!")
                a = first_player()
                b = third_player()


    # Tie between Second and Third
    elif second_player_res == third_player_res:
        print ("Second and Third player had a tie! Roll again! The First player is through to next round!\n")
        a = second_player()
        b = third_player()
        while True:
            if a > b:
                print ("Third player is played out! First and Second player go to Round 2!\n")
                first_vs_second()
                break
            if b > a:
                print ("Second player is played out! First and Third player go to Round 2!\n")
                first_vs_third()
                break
            if a == b:
                print ("Tie! Roll again!")
                a = second_player()
                b = third_player()


# ---- Functions for Round 2 matches ----

def first_vs_third():
    a = first_player()
    b = third_player()
    a_name = "First player"
    b_name = "Third player"
    second_round(a,b,a_name,b_name)

def first_vs_second():
    a = first_player()
    b = second_player ()
    a_name = "First player"
    b_name = "Second player"
    second_round(a,b, a_name, b_name)

def second_vs_third():
    a = second_player()
    b = third_player ()
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

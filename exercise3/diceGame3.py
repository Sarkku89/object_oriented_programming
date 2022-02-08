# File:         diceGame3.py
# Author: Sarianna Junnila
# Description: A dice game with three players, one dice and two rounds. 
#   In the first round two of the highest numbers will go through,
#   and if there two of the same lower number and same color dice, they will roll again
#   If only one of the players in tie gets Blue dice, she/he will go to next round.
#   In the Round 2, the player with higher number wins 
#   and in a tie, if only one has a Blue dice she/he will win even with the same number.

import random

# ---- Class definition ----

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
    
# Method for getting a color for the dice randomly 

    def color_of_the_dice(self):
        if random.randint(0,1) == 0:
            self.color = "Red"
        else:
            self.color = "Blue"

# Methods for getting the value and the color of the dice

    def get_value(self):
        return self.value
    
    def get_color(self):
        return self.color



# ---- Instances for the class (three different players) ----

def first_player():

    first_player = Dice()
    first_player.roll_the_dice()
    first_player.color_of_the_dice()
    dice_color = first_player.get_color()
    first_player_res = int(first_player.get_value())
    return first_player_res, dice_color

def second_player():

    second_player = Dice()
    second_player.roll_the_dice()
    second_player.color_of_the_dice()
    dice_color = second_player.get_color()
    second_player_res = int(second_player.get_value())
    return second_player_res, dice_color

    
def third_player():

    third_player = Dice()
    third_player.roll_the_dice()
    third_player.color_of_the_dice()
    dice_color = third_player.get_color()
    third_player_res = int(third_player.get_value())
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

        # If First and Second player get a "lower" tie in first round
        elif first_color == second_color:
            if first_color == second_color == "Blue":
                print ("All players got the same number. The players with Blue dices win the round! Sorry Third player, you are out!\n")
                first_vs_second()
            else:
                print ("All players got the same number. Third player gets trough to Round 2 with Blue dice.\n")
                print ("First and Second player will roll again!\n")
                first_player_res = first_player()[0]
                second_player_res = second_player()[0]
                first_color = first_player()[1]
                second_color = second_player()[1]
                print ("First player got", first_player_res)
                print ("Second player got", second_player_res, "\n")
                tie_with_colors_fs(first_player_res, second_player_res, first_color, second_color)


        # If First and Third player get a "lower" tie in first round
        elif first_color == third_color:
            if first_color == third_color == "Blue":
                print ("All players got the same number. The players with Blue dices win the round! Sorry Second player, you are out!\n")
                first_vs_second()
            else:
                print ("All players got the same number. Second player gets trough to Round 2 with Blue dice.\n")
                print ("First and Third player will roll again!\n")
                first_player_res = first_player()[0]
                third_player_res = third_player()[0]
                first_color = first_player()[1]
                third_color = third_player()[1]
                print ("First player got", first_player_res)
                print ("Third player got", third_player_res, "\n")
                tie_with_colors_ft(first_player_res, third_player_res, first_color, third_color)

       
        # If Second and Third player get a "lower" tie in first round
        elif second_color == third_color:
            if second_color == third_color == "Blue":
                print ("All players got the same number. The players with Blue dices win the round! Sorry First player, you are out!\n")
                second_vs_third()
            else:
                print ("All players got the same number. First player gets trough to Round 2 with Blue dice.\n")
                print ("Second and Third player will roll again!\n")
                second_player_res = second_player()[0]
                third_player_res = third_player()[0]
                second_color = second_player()[1]
                third_color = third_player()[1]
                print ("Second player got", second_player_res)
                print ("Third player got", third_player_res, "\n")
                tie_with_color_st(second_player_res, third_player_res, second_color, third_color)        


        # If all players get same number but only First and Third player have Blue dice
        elif first_color == third_color == "Blue":
            print ("All players got the same number. The players with blue dices win the round! Sorry Second player, you are out!")
            first_vs_third()

        # If all players get same number but only First and Third player have Blue dice
        elif second_color == third_color == "Blue":
            print ("All players got the same number. The players with blue dices win the round! Sorry First player, you are out!")
            second_vs_third()


    # Tie between First and Second player. 
    elif first_player_res == second_player_res:
        print ("The Third player is through to next round!\n")
        if first_color == "Blue" or second_color == "Blue":
            if first_color == "Blue" and second_color == "Red":
                print ("First player has a Blue dice and will continue to Round 2!\n")
                first_vs_third()
            if second_color == "Blue" and first_color == "Red":
                print ("Second player has a Blue dice and will continue to Round 2!\n")
                second_vs_third()
            else:
                print ("Tie between First and Second player! Please roll again!\n")
                first_player_res = first_player()[0]
                second_player_res = second_player()[0]
                first_color = first_player()[1]
                second_color = second_player()[1]
                print ("First player got", first_player_res)
                print ("Second player got", second_player_res, "\n")
                tie_with_colors_fs(first_player_res, second_player_res, first_color, second_color)
                
        else:
            print ("A tie between First and Second player. Please roll again!\n")
            a = first_player()[0]
            b = second_player()[0]
            print ("First player got", a)
            print ("Second player got",b)
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
                    a = first_player()[0]
                    b = third_player()[0]


    # Tie between First and Third player
    elif first_player_res == third_player_res:
        print ("The Second player is through to next round!\n")
        if first_color == "Blue" or third_color == "Blue":
            if first_color == "Blue" and third_color == "Red":
                print ("First player has a Blue dice and will continue to Round 2!\n")
                first_vs_second()
            if third_color == "Blue" and first_color == "Red":
                print ("Third player has a Blue dice and will continue to Round 2!\n")
                second_vs_third()

            else:
                print ("Tie between First and Third player! Please roll again!\n")
                first_player_res = first_player()[0]
                third_player_res = third_player()[0]
                first_color = first_player()[1]
                third_color = third_player()[1]
                print ("First player got", first_player_res)
                print ("Third player got", third_player_res, "\n")
                tie_with_colors_ft(first_player_res, third_player_res, first_color, third_color)

        else:
            print ("A tie between First and Third player. Please roll again!\n")
            a = first_player()[0]
            b = third_player()[0]
            print ("First player got", a)
            print ("Third player got",b)
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
                    a = first_player()[0]
                    b = third_player()[0]


    # Tie between Second and Third

    elif second_player_res == third_player_res:
        print ("The First player is through to next round!\n")
        if second_color == "Blue" or third_color == "Blue":
            if second_color == "Blue" and third_color == "Red":
                print ("Second player has a Blue dice and will continue to Round 2!\n")
                first_vs_second()
            if third_color == "Blue" and second_color == "Red":
                print ("Third player has a Blue dice and will continue to Round 2!\n")
                first_vs_third()
            else:
                print ("Tie with Second and Third player. Please roll again!\n")
                second_player_res = second_player()[0]
                third_player_res = third_player()[0]
                second_color = second_player()[1]
                third_color = third_player()[1]
                print ("Second player got", second_player_res)
                print ("Third player got", third_player_res, "\n")
                tie_with_color_st(second_player_res, third_player_res, second_color, third_color)   

        else:
            print ("A tie between Second and Third player. Please roll again!\n")
            a = second_player()[0]
            b = third_player()[0]
            print ("Second player got", a)
            print ("Third player got",b)
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
                    a = second_player()[0]
                    b = third_player()[0]


# ---- Functions for Round 1 ties ----

    #Tie with Second and Third player

def tie_with_color_st(second_player_res, third_player_res, second_color, third_color):
    while True:
        if second_player_res > third_player_res:
            print ("Second player will join First player in the Round 2\n")
            second_vs_third()
            break
        elif third_player_res > second_player_res:
            print ("Third player will join First player in the Round 2\n")
            first_vs_third()
            break
        elif second_player_res == third_player_res:
            if second_color == "Blue" and third_color == "Red":
                print ("Tie! But with Blue color dice Second player will go to Round 2!\n")
                first_vs_second()
                break
            elif second_color == "Blue" and third_color == "Red":
                print ("Tie! But with Blue color dice Second player will go to Round 2!\n")
                first_vs_second()
                break
            else:
                print ("Same number and same color! Lets roll again!\n")
                third_player_res = third_player()[0]
                second_player_res = second_player()[0]
                third_color = third_player()[1]
                second_color = second_player()[1]   


    # Tie with First and Third player

def tie_with_colors_ft(first_player_res, third_player_res, first_color, third_color):
    while True:
        if first_player_res > third_player_res:
            print ("First player will join Second player in the Round 2\n")
            first_vs_third()
            break
        elif third_player_res > first_player_res:
            print ("Third player will join Second player in the Round 2\n")
            second_vs_third()
            break
        elif first_player_res == third_player_res:
            if first_color == "Blue" and third_color == "Red":
                print ("Tie! But with Blue color dice First player will go to Round 2!\n")
                first_vs_third()
                break
            if third_color == "Blue" and first_color == "Red":
                print ("Tie! But with Blue color dice Third player will go to Round 2!\n")
                second_vs_third()
                break
            else:
                print ("Same number and same color! Lets roll again!\n")
                first_player_res = first_player()[0]
                third_player_res = third_player()[0]
                first_color = first_player()[1]
                third_color = third_player()[1]    


    #Tie with First and Second player

def tie_with_colors_fs(first_player_res, second_player_res, first_color, second_color):
    while True:
        if first_player_res > second_player_res:
            print ("First player will join Third player in the Round 2\n")
            first_vs_third()
            break
        elif second_player_res > first_player_res:
            print ("Second player will join Third player in the Round 2\n")
            second_vs_third()
            break
        elif first_player_res == second_player_res:
            if first_color == "Blue" and second_color == "Red":
                print ("Tie! But with Blue color dice First player will go to Round 2!\n")
                first_vs_third()
                break
            if second_color == "Blue" and first_color == "Red":
                print ("Tie! But with Blue color dice Second player will go to Round 2!\n")
                second_vs_third()
                break
            else:
                first_player_res = first_player()[0]
                second_player_res = second_player()[0]
                first_color = first_player()[1]
                second_color = second_player()[1]



# ---- Functions for Round 2 matches ----

def first_vs_third():
    a = first_player()[0]
    b = third_player()[0]
    a_name = "First player"
    b_name = "Third player"
    a_color = first_player()[1]
    b_color = third_player()[1]
    second_round(a,b,a_name,b_name, a_color, b_color)

def first_vs_second():
    a = first_player()[0]
    b = second_player ()[0]
    a_name = "First player"
    b_name = "Second player"
    a_color = first_player()[1]
    b_color = second_player()[1]
    second_round(a,b,a_name,b_name, a_color, b_color)

def second_vs_third():
    a = second_player()[0]
    b = third_player ()[0]
    a_name = "Second player"
    b_name = "Third player"
    a_color = second_player()[1]
    b_color = third_player()[1]
    second_round(a,b,a_name,b_name, a_color, b_color)


# ---- Function for the Round 2 ----
def second_round(a,b, a_name, b_name, a_color, b_color):
    print(a_name,"got", a_color, a)
    print(b_name,"got",b_color, b)
    while True:
        if a > b:
            print ("The winner is", a_name, "\n")
            break
        elif b > a:
            print ("The winner is", b_name, "\n")
            break
        elif a == b:
            if a_color == "Blue" and b_color == "Red":
                print ("The winner is", a_name, "\n")
                break
            if b_color == "Blue" and a_color == "Red":
                print ("The winner is", b_name, "\n")
                break
            if a_color == b_color:
                print ("Tie! Roll again!")
                if a_name == "First player" and b_name == "Third player":
                    first_vs_third()
                    break
                elif a_name == "First player" and b_name == "Second player":
                    first_vs_second()
                    break
                else:
                    second_vs_third()
                    break



# --- Calling the game function --- 
play_the_game()

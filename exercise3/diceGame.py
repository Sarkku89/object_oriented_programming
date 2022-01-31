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


# ----- The first rounds with clear winners -----

# Third player is played out in the first round  

    if first_player_roll > third_player_roll and second_player_roll > third_player_roll :
        print ("The Third player is out of the game! First and Second player rematch!")

    # Second round with First and Second player
        
        first_player_roll = first_player()
        print ("Second round: First player gets:", first_player_roll)
        second_player_roll = second_player()
        print ("Second round: Second player gets:", second_player_roll)
        while True:
            if first_player_roll > second_player_roll:
                print ("The First player won the game!")
                break
            if second_player_roll > first_player_roll:
                print ("The Second player won the game!")
                break
            if first_player_roll == second_player_roll:
                print ("Tie! Roll again!")
                first_player_roll = first_player()
                print ("Second round: First player gets:", first_player_roll)
                second_player_roll = second_player()
                print ("Second round: Second player gets:", second_player_roll)



# First player is played out in the first round 

    elif second_player_roll > first_player_roll and third_player_roll > first_player_roll:
        print ("The First player is out of the game! Second and Third player rematch!")

    # Second round with Second and Third player

        second_player_roll = second_player()
        print ("Second round: Second player gets:", second_player_roll)
        third_player_roll = third_player()
        print ("Second round: Third player gets:", third_player_roll)
        while True:
            if second_player_roll > third_player_roll:
                print ("The Second player won the game!")
                break
            if third_player_roll > second_player_roll:
                print ("The Third player won the game!")
                break
            if second_player_roll == third_player_roll:
                print ("Tie! Roll again!")
                second_player_roll = second_player()
                print ("Second round: Second player gets:", second_player_roll)
                third_player_roll = third_player()
                print ("Second round: Third player gets:", third_player_roll)



# Second player is played out in the first round 

    elif first_player_roll > second_player_roll and  third_player_roll > second_player_roll:
        print ("The Second player is out of the game! First and Third player rematch!")

    # Second round with first and third player

        first_player_roll = first_player()
        print ("Second round: First player gets:", first_player_roll)
        third_player_roll = third_player()
        print ("Second round: Third player gets:", third_player_roll)

        while True:
            if first_player_roll > third_player_roll:
                print ("The First player won the game!")
                break
            if third_player_roll > first_player_roll:
                print ("The Third player won the game!")
                break
            if first_player_roll == third_player_roll:
                print ("Tie! Roll again!")
                first_player_roll = first_player()
                print ("Second round: First player gets:", first_player_roll)
                third_player_roll = third_player()
                print ("Second round: Third player gets:", third_player_roll)

# ---- If all players get same number in the first round ----
    elif first_player_roll == second_player_roll == third_player_roll:
        print ("All players rolled the same number! Rematch!")
        play_the_game()

# ---- If there is only a one winner of first round and tie with 2 dices ----

    elif first_player_roll == second_player_roll or second_player_roll == third_player_roll  or first_player_roll == third_player_roll:

    # Tie between First and Second player

        if first_player_roll == second_player_roll:
            print ("First and Second player had a tie! Roll again! The Third player is through to next round!")
            first_player_roll = first_player()
            print ("First player gets: ", first_player_roll)
            second_player_roll = second_player ()
            print ("Second player gets:", second_player_roll)

            while True:
                if first_player_roll > second_player_roll:
                    print ("Second player is played out! First and Third player go to Round 2!")

                # Second round with First and Third player

                    first_player_roll = first_player()
                    print ("Second round: First player gets:", first_player_roll)
                    third_player_roll = third_player()
                    print ("Second round: Third player gets:", third_player_roll)

                    while first_player_roll > second_player_roll or second_player_roll > first_player_roll:
                        if first_player_roll > third_player_roll:
                            print ("The First player won the game!")
                            break
                        if third_player_roll > first_player_roll:
                            print ("The Third player won the game!")
                            break
                        if first_player_roll == third_player_roll:
                            print ("Tie! Roll again!")
                            first_player_roll = first_player()
                            print ("Second round: First player gets:", first_player_roll)
                            third_player_roll = third_player()
                            print ("Second round: Third player gets:", third_player_roll)

                if second_player_roll > first_player_roll:
                    print ("First player is played out! Second and Third player rematch!")
                
                # Second round with Second and Third player
                    second_player_roll = second_player()
                    print ("Second round: The Second player gets:", second_player_roll)
                    third_player_roll = third_player()
                    print ("Second round: Third player gets:", third_player_roll)

                    while second_player_roll > third_player_roll or third_player_roll > second_player_roll:
                        if second_player_roll > third_player_roll:
                            print ("The Second player won the game!")
                            break
                        if third_player_roll > second_player_roll:
                            print ("The Third player won the game!")
                            break
                        if second_player_roll == third_player_roll:
                            print ("Tie! Roll again!")
                            second_player_roll = second_player()
                            print ("Second round: Second player gets:", second_player_roll)
                            third_player_roll = third_player()
                            print ("Second round: Third player gets:", third_player_roll)

    # Tie between First and Third player

    elif first_player_roll == third_player_roll:
            print ("First and Third player had a tie! Roll again! The Second player is through to next round!")
            first_player_roll = first_player()
            print ("First player gets: ", first_player_roll)
            third_player_roll = third_player ()
            print ("Third player gets:", third_player_roll)

            while True :
                if first_player_roll > third_player_roll:
                    print ("Third player is played out! First and Second player go to Round 2!")

                # Second round with First and Second player

                    first_player_roll = first_player()
                    print ("Second round: First player gets:", first_player_roll)
                    second_player_roll = second_player()
                    print ("Second round: Second player gets:", second_player_roll)

                    while first_player_roll > second_player_roll or second_player_roll > first_player_roll:
                        if first_player_roll > third_player_roll:
                            print ("The First player won the game!")
                            break
                        if second_player_roll > first_player_roll:
                            print ("The Third player won the game!")
                            break
                        if first_player_roll == second_player_roll:
                            print ("Tie! Roll again!")
                            first_player_roll = first_player()
                            print ("Second round: First player gets:", first_player_roll)
                            second_player_roll = second_player()
                            print ("Second round: Second player gets:", second_player_roll)

                if second_player_roll > first_player_roll:
                    print ("First player is played out! Second and Third player rematch!")
                
                # Second round with Second and Third player
                    second_player_roll = second_player()
                    print ("Second round: Second player gets:", second_player_roll)
                    third_player_roll = third_player()
                    print ("Second round: Third player gets:", third_player_roll)

                    while second_player_roll > third_player_roll or third_player_roll > second_player_roll:
                        if second_player_roll > third_player_roll:
                            print ("The Second player won the game!")
                            break
                        if third_player_roll > second_player_roll:
                            print ("The Third player won the game!")
                            break
                        if second_player_roll == third_player_roll:
                            print ("Tie! Roll again!")
                            second_player_roll = second_player()
                            print ("Second round: Second player gets:", second_player_roll)
                            third_player_roll = third_player()
                            print ("Second round: Third player gets:", third_player_roll)
            
    # Tie between Second and Third player

    elif second_player_roll == third_player_roll:
            print ("Second and Third player had a tie! Roll again! The First player is through to next round!")
            second_player_roll = second_player()
            print ("Second player gets: ", first_player_roll)
            third_player_roll = third_player ()
            print ("Third player gets:", third_player_roll)

            while True:
                if second_player_roll > third_player_roll:
                    print ("Third player is played out! First and Second player go to Round 2!")

                # Second round with First and Second player

                    first_player_roll = first_player()
                    print ("Second round: First player gets:", first_player_roll)
                    second_player_roll = second_player()
                    print ("Second round: Second player gets:", second_player_roll)

                    while first_player_roll > second_player_roll or second_player_roll > first_player_roll:
                        if first_player_roll > third_player_roll:
                            print ("The First player won the game!")
                            break
                        if second_player_roll > first_player_roll:
                            print ("The Third player won the game!")
                            break
                        if first_player_roll == second_player_roll:
                            print ("Tie! Roll again!")
                            first_player_roll = first_player()
                            print ("Second round: First player gets:", first_player_roll)
                            second_player_roll = second_player()
                            print ("Second round: Second player gets:", second_player_roll)

                if third_player_roll > second_player_roll:
                    print ("Second player is played out! First and Third player rematch!")
                
                # Second round with First and Third player

                    first_player_roll = first_player()
                    print ("Second round: First player gets:", first_player_roll)
                    third_player_roll = third_player()
                    print ("Second round: Third player gets:", third_player_roll)

                    while first_player_roll > second_player_roll or second_player_roll > first_player_roll:

                        if first_player_roll > third_player_roll:
                            print ("The First player won the game!")
                            break
                        if third_player_roll > first_player_roll:
                            print ("The Third player won the game!")
                            break
                        if first_player_roll == third_player_roll:
                            print ("Tie! Roll again!")
                            first_player_roll = first_player()
                            print ("Second round: First player gets:", first_player_roll)
                            third_player_roll = third_player()
                            print ("Second round: Third player gets:", third_player_roll)



play_the_game()

    

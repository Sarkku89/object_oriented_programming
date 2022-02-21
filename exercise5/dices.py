# File:   dices.py
# Author: Sarianna Junnila
# Description:  Dice game for multiple player. User inputs the player amount. 
#   The dices are thrown trice and the results of each player are summed.
#   If there is a tie between the highest results the amount of tieing players will play again.

import diceClass

# Defining the main function
def main(number_of_players):
    sum_list = []
    dice_list = make_list(number_of_players)
    
    print ("\n")

# The sum_list get as many zeros as there are players
    for count in range(0,number_of_players-1):
        sum_list.append(0)

# The game has three rounds
    for count in range(0,3):
        round_result_list = []
        player = 0

# The players will have a roll each on every round
        for item in dice_list:
            item.roll_dice(6)
            result = item.get_value()
            round_result_list.append(result)
            player +=1
            print ("On round", count+1, "the player", player, "got", result)

# In the end of each round the sum_the_result function is called
        sum_the_result(round_result_list, sum_list)
        
        print("\n")
    
# After the rounds and counting the sums the display function is called
    display_sum_list(sum_list)

# Defining a function for displaying the results after the results are summed
def display_sum_list(a_list):
    player = 0
    for item in a_list:
        player +=1
        print ("The total result of player", player, "is", item)

# Calling the function to conclude the winner
    conclude_winner(a_list)

# Defining a function for concluding the winner
def conclude_winner(a_list):

    # If there is two or more of the maximum result the main 
    #   function is called with the number of tied players

    if a_list.count(max(a_list)) >= 2: 
        print("\nThe players have tied! They play again!\n")
        number_of_players = a_list.count(max(a_list))
        main(number_of_players+1)

    # Otherwise the winner is printed
    else:
        print ("The player", a_list.index(max(a_list))+1, "wins!")
    
# Defining a function to maka a list of Dice objects            
def make_list(number_of_players):
    dice_list = []
    print ("We have", number_of_players-1, "players in the game! Please roll your dice!")
    for count in range(1,number_of_players):
        new_dice= diceClass.Dice()
        dice_list.append(new_dice)
        
    return dice_list
    
# Defining a function to count the sum of the rolls for each player
def sum_the_result(round_result_list, sum_list):
        x = 0
        for i in round_result_list:
            sum_list[x] = round_result_list[x] + sum_list[x]
            
            x += 1
        return sum_list

            
# Calling the main gunction
main(number_of_players = int(input("\nPlease insert the number of players: "))+1)
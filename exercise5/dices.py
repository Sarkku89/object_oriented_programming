# File:   dices.py
# Author: Sarianna Junnila
# Description:  

import diceClass

def main(number_of_players):
    sum_list = []
    round_result_list =[]
    

    dice_list = make_list(number_of_players)
    
    print ("\n")

    for count in range(0,number_of_players-1):
        sum_list.append(0)

    for count in range(0,3):
        round_result_list = []
        player = 0
        for item in dice_list:
            item.roll_dice(6)
            result = item.get_value()
            round_result_list.append(result)
            player +=1
            print ("On round", count+1, "the player", player, "got", result)
        sum_the_result(round_result_list, sum_list)
        print("\n")
    

    display_list(sum_list)


def display_list(a_list):
    player = 0
    for item in a_list:
        player +=1
        print ("The total result of player", player, "is", item)
    conclude_winner(a_list)

def conclude_winner(a_list):
    if a_list.count(max(a_list)) >= 2:
        print("\nThe players have tied! They play again!\n")
        number_of_players = a_list.count(max(a_list))
        main(number_of_players+1)
    else:
        print ("The player", a_list.index(max(a_list))+1, "wins!")
    
            
def make_list(number_of_players):
    dice_list = []
    print ("We have", number_of_players-1, "players in the game! Please roll your dice!")
    for count in range(1,number_of_players):
        new_dice= diceClass.Dice()
        dice_list.append(new_dice)
        
    return dice_list
    
def sum_the_result(round_result_list, sum_list):
        x = 0
        for i in round_result_list:
            sum_list[x] = round_result_list[x] + sum_list[x]
            
            x += 1
        return sum_list

            

main(number_of_players = int(input("\nPlease insert the number of players: "))+1)
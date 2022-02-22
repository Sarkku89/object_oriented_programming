# File:   playerMain.py
# Author: Sarianna Junnila
# Description:  Main function combining 
#   dices and player into a dictionary and printing it.

import playerClass

def main():
    player1 = playerClass.Player(first_name="Clark", last_name= "Kent", id=1)
    player2 = playerClass.Player(first_name="Bruce", last_name="Wayne", id= 2)
    player3 = playerClass.Player(first_name="Peter", last_name="Parker", id =3)
    dice1 = playerClass.Dice()
    roll1 = dice1.roll_dice(6)
    dice2 = playerClass.Dice()
    roll2 = dice2.roll_dice(6)
    dice3 = playerClass.Dice()
    roll3 = dice3.roll_dice(6)

    players = {
        player1.id : dice1.get_value(),
        player2.id : dice2.get_value(),
        player3.id : dice3.get_value()
    }
    print("\n")
    print (player1, "rolled", players[player1.id])
    print (player2, "rolled", players[player2.id])
    print (player3, "rolled", players[player3.id])
    print("\n")
    

main()
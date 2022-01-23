#File name: rockPaperSciccors.py
#Author: Sarianna Junnila
#Description: A simple game of rock, paper and scissors. 
# Player can pick one of them. First one to pick three winning tools wins.

import random 

def ro_pa_sc():

    user_wins = 0
    computer_wins = 0
    options = ["rock" , "paper" , "scissors"]

    print ("This the game 'Rock, Paper and Scissors'. You're playing against the computer. \n The one who wins 3 games wins.  Please use small letters when typing your pick \n")

    while user_wins < 3 and computer_wins < 3:
        user_pick = input("Please pick: rock, paper or scissors? ")
        comp_pick = options[random.randint(0,2)]

    # Ties. If both the user and the computer picks the same tool.

        if user_pick == "rock" and comp_pick == "rock":
            print ("Tie. Both picked rock. Please pick again!")
            print ( "Computer", computer_wins,"- You",user_wins, "\n")
            continue

        if user_pick == "paper" and comp_pick == "paper":
            print ("Tie. Both picked paper. Please pick again!")
            print ( "Computer", computer_wins,"- You",user_wins, "\n")
            continue

        if user_pick == "scissors" and comp_pick == "scissors":
            print ("Tie. Both picked scissors. Please pick again!")
            print ( "Computer", computer_wins,"- You",user_wins, "\n")
            continue


    # Computer wins.

        if user_pick == "rock" and comp_pick == "paper":
            computer_wins = computer_wins + 1
            print ("Computer picked paper. Computer wins!")
            print ( "Computer", computer_wins,"- You",user_wins, "\n")
            continue
        
        if user_pick == "scissors" and comp_pick == "rock":
            computer_wins = computer_wins + 1
            print ("Computer picked rock. Computer wins!")
            print ( "Computer", computer_wins,"- You",user_wins,"\n")
            continue

        if user_pick == "paper" and comp_pick == "scissors":
            computer_wins = computer_wins + 1
            print ("Computer picked scissors. Computer wins!")
            print ( "Computer", computer_wins,"- You",user_wins,"\n")
            continue


    # User wins.

        if user_pick == "scissors" and comp_pick == "paper":
            user_wins = user_wins + 1
            print ("Computer picked paper. You win!")
            print ( "Computer", computer_wins,"- You",user_wins,"\n")
            continue

        if user_pick == "rock" and comp_pick == "scissors":
            user_wins = user_wins + 1
            print ("Computer picked scissors. You win!")
            print ( "Computer", computer_wins,"- You",user_wins,"\n")
            continue

        if user_pick == "paper" and comp_pick == "rock":
            user_wins = user_wins + 1
            print ("Computer picked rock. You win!")
            print ( "Computer", computer_wins,"- You",user_wins,"\n")
            continue

        if user_pick != "paper" or user_pick != "rock" or user_pick != "scissors":
            print ("Typing error. Please type your pick in small letters. \nYou can only pick rock, paper or scissors.\n")
            continue

    else:
        if user_wins == 3:
            print ("Congratulations! You won", user_wins, "to", computer_wins, "! Please play again!", "\n")
            ro_pa_sc()

        if computer_wins == 3:
            print ("Sorry, the computer won by", computer_wins, "to", user_wins, "! Please play again!", "\n")
            ro_pa_sc()


ro_pa_sc()
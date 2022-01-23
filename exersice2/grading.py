#File name: grading.py
#Author: Sarianna Junnila
#Description: A program which gives the user his/hers grande according to the points he/she inputs.

def grading_the_course():
    points = int(input("Write your points here: "))
    if points >= 0 and points < 60:
        print ("Unfortunately you failed the course")
    elif points >= 60 and points < 72:
        print ("Your grade is 1")
    elif points >= 72 and points < 84:
        print ("Your grade is 2")
    elif points >= 84 and points < 96:
        print ("Your grade is 3")
    elif points >= 96 and points < 108:
        print ("Your grage is 4")
    elif points >= 108 and points < 121: 
        print ("Congratulation! Your grade is 5")
    else:
        print ("Please check that you typed your points correctly.")
        grading_the_course()

grading_the_course()


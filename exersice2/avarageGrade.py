#File name: avarageGrade.py
#Author: Sarianna Junnila
#Description: A program which gives the user the avarage grade 
# of the course and saves the inputs in a dictionary.

def avar_grade():
    grade_table = {}
    grade_list = []
    key = input("Write your name here: ")
    value = int(input("Write your grade here: "))
    if value >= 0 and value <= 5:
        grade_table[key] = value
        grade_list.append(value)
        avarage = sum(grade_list)
    else:
        print ("Your grade must be between 0 and 5. Please try again.")
        return avar_grade()

    while input ("Do you want to add more grades? y/n ") == "y":
        key = input("Write your name here: ")
        value = int(input("Write your grade here: "))
        grade_table[key] = value
        grade_list.append(value)
        avarage = sum(grade_list) / len(grade_list)

    if avarage == 0:
        print ("Sorry, everybody has failed this course. The avarage grade is 0.")
    else:
        print ("The average grade for this course is: ", avarage)

avar_grade()
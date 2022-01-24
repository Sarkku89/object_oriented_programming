#File name: avarageGrade.py
#Author: Sarianna Junnila
#Description: A program which gives the user the avarage grade of the course and saves the inputs in a dictionary.

grade_table = {}
grade_list = []

def avarage_grade():
    avarage = sum(grade_list)
    key = input("Write your name here: ")
    value = int(input("Write your grade here: "))
    grade_table[key] = value
    grade_list.append(value)
    avarage = (value + avarage) / len(grade_list)
    print ("The average grade for this course is: ", avarage)
    print (grade_table)
    print (grade_list)
    avarage_grade()

avarage_grade()

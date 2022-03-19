# File:   quiz.py
# Author: Sarianna Junnila
# Description: A quiz of countries by capital cities. The countries and cities are first
#   put into a dictionary and then randomly picked. Ten questions are asked
#   and then the total points are presented to the user.

import random

# Definition for a funtion to put all the countries into a dictionary


def make_dictionary():
    a_dictionary = {}
    try:
        a_file = open(
            "C:\\Users\\Sarkku\\Documents\\GitHub\\object_oriented_programming\\exercise7\\task6\\countries.txt")
        for line in a_file:
            value, key = line.split()
            a_dictionary[key] = value
        return a_dictionary
    except IOError:
        print("File not accessible")

# The quiz definition


def quiz():
    country_dict = make_dictionary()
    points = 0
    q = 0
    while q < 10:
        
            country = random.choice(list(country_dict.keys()))
            quess = input("Which country's capital is {country}? ".format(**locals()))
            try:
                if quess not in country_dict.values():
                    q += 1
                if quess == country_dict[country]:
                    print("Correct!")
                    points += 1
                    q += 1
                    country_dict.pop(country)
            except:
                raise Exception("Wrong! The correct answer is",country_dict[country])
                

    print("You got", points, "right out of 10! ")


# Calling the quizz function

quiz()
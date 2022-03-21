# File:   quiz.py
# Author: Sarianna Junnila
# Description: A quiz of countries or capital cities. The countries and cities are first
#   put into a dictionary and then randomly picked. Ten questions are asked
#   and then the total points are presented to the user.

import random

# Definition for a funtion to put all the countries into a dictionary


def make_dictionaryA():
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


def make_dictionaryB():
    a_dictionary = {}
    try:
        a_file = open(
            "C:\\Users\\Sarkku\\Documents\\GitHub\\object_oriented_programming\\exercise7\\task6\\countries.txt")
        for line in a_file:
            key, value = line.split()
            a_dictionary[key] = value
        return a_dictionary
    except IOError:
        print("File not accessible")

# The quiz definition


def quiz():
    points = 0
    q = 0
    while True:
        try:
            choice = int(
                input("Do you want to quess capitals or countries? Countries: 1 Capitals:2 "))
            if choice == 1:
                country_dict = make_dictionaryA()
                while q < 10:
                    country = random.choice(list(country_dict.keys()))
                    quess = input(
                        "Which country's capital is {country}? Please use capital letters.".format(**locals()))
                    if quess == country_dict[country]:
                        print("Correct!")
                        points += 1
                        q += 1
                        country_dict.pop(country)
                    else:
                        print("Wrong! The correct answer is",
                            country_dict[country])
                        q += 1
                        country_dict.pop(country)
                break

            elif choice == 2:
                country_dict = make_dictionaryB()
                while q < 10:
                    country = random.choice(list(country_dict.keys()))
                    quess = input(
                        "What is the capital of {country}? Please use capital letters. ".format(**locals()))
                    if quess == country_dict[country]:
                        print("Correct!")
                        points += 1
                        q += 1
                        country_dict.pop(country)
                    else:
                        print("Wrong! The correct answer is",
                            country_dict[country])
                        q += 1
                        country_dict.pop(country)
                break
            else:
                print("Please enter either 1 or 2")
            

        except:
            print("Please enter either 1 or 2")

    print("You got", points, "right out of 10! ")
        

# Calling the quizz function

quiz()

# File:   exceptionHandling.py
# Author: Sarianna Junnila
# Description: Testing five different types of exceptions


import math

# When there is a problem with item types.
def type_error():
    a = 1
    b = "String"
    try:
        print(a+b)
    except TypeError:
        print("TypeError! You can't concatenate integers and strings! ")

type_error()


# When trying to divide with zero
def division(number):
    a= 2
    b= number
    try:
        print(2/number)
    except ZeroDivisionError:
        print("You can't use zero as a divider!")

division(0)


# When given a right type of argument, but wrong value
def value_error():
    try:
        arg = -1
        math.sqrt(arg)
    except ValueError:
        print("Only positive numbers!")

value_error()


# When giving indexes out of range of the list
def index_error(index):
    list = ["A", "B", "C", "D"]
    try:
        print(list[index])
    except IndexError:
        print("There are not enough items in the list for that index!")

index_error(5)


# When given faulty file name or path
def not_found():
    try:
        a_file = open("counties.txt")

    except FileNotFoundError:
        print("File was not found...")

not_found()
#File name: printing_lists.py
#Author: Sarianna Junnila
#Description: Takes given input items (numbers or strings) and prints the list out

from random import randint

number_list= []
for x in range (1,11):
    input_number=input("Give me a number, please ")
    number_list.append(input_number)

print("Thank you! Your numbers are:" , number_list)

string_list=[]
for x in range (1,11):
    input_string=input("Give me a word, please ")
    string_list.append(input_string)

print("Thank you! Your words are:" , string_list)

rand_number_list= []
for x in range (1,11):
    random_number=randint(0,100)
    rand_number_list.append(random_number)

print(rand_number_list)
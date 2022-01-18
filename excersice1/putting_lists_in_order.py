#File name: putting_lists_in_order.py
#Author: Sarianna Junnila
#Description: Orders given lists into numerical or aplhabetical order.

"""Prints a list of given ten integers"""
number_list= []
for x in range (1,11):
    input_number=int(input("Give me a number, please "))
    number_list.append(input_number)
number_list.sort()
print("Thank you! Your numbers are:" , number_list)


"""Prints a list of given ten strings"""
string_list=[]
for x in range (1,11):
    input_string=input("Give me a word, please ")
    string_list.append(input_string)

string_list.sort()
print("Thank you! Your words are:" , string_list)
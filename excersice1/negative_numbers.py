#File name: negative_numbers.py
#Author: Sarianna Junnila
#Description: Takes input integers, until the user gives 0. Then prints the number of the negative integers.

neg_number_list = []
pos_number_list = []

def counting_the_negative():
    while True:
        input_number = int(input("Give me a number, please "))
        if input_number < 0:
            neg_number_list.append(input_number)
            continue
            
        if input_number > 0:
           pos_number_list.append(input_number)
           continue

        else:
            count = len(neg_number_list)
            return print("There were" ,count, "negative numbers")
            break
            

counting_the_negative()
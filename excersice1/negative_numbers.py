#File name: negative_numbers.py
#Author: Sarianna Junnila
#Description: Takes input integers, until the user gives 0. Then prints the number of the negative integers.

neg_number_list = []
def converting_to_negative():
    
    input_number = int(input("Give me a number, please "))
    if input_number > 0:
        converting_to_negative()
        
    
    if input_number < 0:
        neg_number_list.append(input_number)
        converting_to_negative()
        

    else:
        count = len(neg_number_list)
        print("There were" ,count, "negative numbers")
                

converting_to_negative()
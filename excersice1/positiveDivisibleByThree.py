#File name: positiveDivisibleByThree.py
#Author: Sarianna Junnila
#Description: Takes input integers, until the user gives 0. 
# Then prints the number of the negative integers and counts the even numbers.
# Then counts the sum of positive integers divisible by 3 and prints it.

neg_number_list = []
pos_number_list = []

def counting_the_sum():
    sum = 0

    for a in pos_number_list:
        if a % 3 == 0:
            sum = sum + a

    return print ("The sum of positive numbers divisible by 3 is ", sum)

def counting_the_even():
    even_count = 0
    new_list = neg_number_list + pos_number_list

    for i in new_list:
        if abs(i) % 2 == 0:
            even_count = even_count + 1

    print ("The number of even numbers is ", even_count)
    counting_the_sum()


def counting_the_negative():
    while True:
        input_number = int(input("Give me a number, please "))

        if input_number < 0:
            neg_number_list.append(input_number)
            continue
            
        elif input_number > 0:
           pos_number_list.append(input_number)
           continue

        else:
            count = len(neg_number_list)
            print("There were" ,count, "negative numbers")
            counting_the_even()
            break
            

counting_the_negative()
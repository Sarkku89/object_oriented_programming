#File name: arithmetic_progression.py
#Author: Sarianna Junnila
#Description: The program takes the maximum value from the user. 
# Then it counts the number of terms used, the sum of these terms and
# the sum of the terms squared


def arithmetic_progg():

    input_max = int(input("Give me a number bigger than 3, please: "))
    a = 3
    list = [3]
    sum = 3
    sum_of_squared = 3 ** 2
    
    while a < (input_max -2) and a != input_max:
        a = a + 3
        list.append(a)
        sum = sum + a
        sum_of_squared = sum_of_squared + a ** 2

    else:     
        print ("The number of terms in AP is: ", len(list))
        print ("The sum of the terms of AP is: ", sum)
        print ("The sum of the terms squared is:", sum_of_squared)
        return


arithmetic_progg()



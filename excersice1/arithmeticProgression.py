#File name: arithmeticProgression.py
#Author: Sarianna Junnila
#Description: A program which counts with arithmetic progression (a+3) 
# until reaches the maximum value or the closesta possible value.
# The program takes the maximum value from the user. 
# Then it counts the number of terms used, the sum of these terms and
# the sum of the terms squared


def arithmetic_progg():

    input_max = int(input("Give me the maximum value, please: "))
    a = 0 
    list_of_terms = []
    sum = 0
    sum_of_squared = 0
    
    while a < (input_max -2) and a != input_max: 
        a = a + 3
        list_of_terms.append(a)
        sum = sum + a
        sum_of_squared = sum_of_squared + a ** 2

    else:
        print ("The terms in AP are:", list_of_terms)
        print ("The number of terms in AP is: ", len(list_of_terms))
        print ("The sum of the terms of AP is: ", sum)
        print ("The sum of the terms squared is:", sum_of_squared)
        return


arithmetic_progg()



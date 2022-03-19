# File:  bakingCookies.py
# Author: Sarianna Junnila
# Description:  Defining functions for baking and freezing cookies

import cookieClass

# Denifing function for baking the cookies
def freeze_the_cookie(cookie):
    cookie.set_frozen(True)
    print("This cookie is frozen!")

# Denifing function for flavoring the cookies
def flavor_the_cookie(cookie):
    flavour = input("Which flavour you want into your cookie?")
    cookie.set_flavour(flavour)
    print("Now this is a", flavour, "cookie!")

# Denifing main function
def cookieMain():

    # Baking the cookies
    print("Lets bake!")
    baked_list = []

    while len(baked_list) < 10:
        try:
            x = int(input("Do you want to bake a cookie? Yes = 1, No = 2 "))
            if x == 1:
                cookie = cookieClass.Cookie(True, False, "")
                baked_list.append(cookie)
                print("Now you have", len(baked_list), "baked cookies!")

            elif x == 2:
                print("Ok! Remember that you need 10 baked cookies...\n At the moment you have", len(
                    baked_list), "baked cookies.")
            else:
                print("Please give only either number 1 or 2!")


        except:
            print("Please give only either number 1 or 2!")


    # Freezing the cookies
    print("\nOk! Time to freeze the cookies!\n")

    frozen_list = []
    cookie_index = 0
    while len(frozen_list) < 10:
        1
        try:
            x = int(input("Do you want to freeze a cookie? Yes = 1, No = 2 "))
            if x == 1:
                freeze_the_cookie(baked_list[cookie_index])
                frozen_list.append(baked_list[cookie_index])
                print("Now you have", len(frozen_list), "frozen cookies!")
                cookie_index += 1

            elif x == 2:
                print("Ok! Remember that you need to freeze 10 cookies...\n At the moment you have", len(
                    frozen_list), "frozen cookies.")
            else:
                print("Please give only either number 1 or 2!")


        except:
            print("Please give only either number 1 or 2!")

    print("\nAll frozen! Now, choose if you want to flavour the cookies somehow.\n")


    # Flavouring the cookies
    for i in frozen_list:
        try:
            x = int(
                input("Do you want to put some toppings to this cookie? Yes = 1, No = 2 "))
            if x == 1:
                flavor_the_cookie(i)

            elif x == 2:
                print("Ok! Let's keep this one basic!")
            
            else:
                print("Please give only either number 1 or 2!")

        except:
            print("Please give only either number 1 or 2!")

    for c in frozen_list:
        print(c)

# Calling the cookieMain function
cookieMain()

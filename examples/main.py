import coin

# Main function definition

def main():

    my_coin = coin.Coin("Tails", "Silver")

    print("This side is up:", my_coin.get_sideup())

    print("Tossing the coin...")
    my_coin.toss_the_coin()

    print("Now this side is up:", my_coin.get_sideup())

    print("Material is ", my_coin.get_material())


# Calling the main function
main()

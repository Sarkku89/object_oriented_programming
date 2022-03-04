import mammals
def main():
    print("\n")
    my_cat = mammals.Cats("Meoww", "raw food", "Einari Halla", "Cat", "Kitty")
    print(my_cat)
    my_cat2 = mammals.Cats("Meoww", "chicken", "Vilja Kilpi", "Cat", "Snowball")
    print(my_cat2)

    my_dog = mammals.Dogs("Wuff", "kibble", "Kerttu Rauta", "Dog", "Blackie")
    print(my_dog)
    my_dog2 = mammals.Dogs("Wuff", "home meals", "Tenho Pirtti", "Dog", "Jack")
    print(my_dog2)
    print("\n")


main()
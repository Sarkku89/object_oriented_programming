# File:  plantClass.py
# Author: Sarianna Junnila
# Description:  Definitions for Plant, flowerless and 
#   other plants, and roses and shops classes

# Plant class definiton
from turtle import color


class Plant:
    def __init__(self, species, height):

        self.species = species
        self.height = height

# Str method
    def __str__(self):
        return str(self.get_species() + " is approximately "
                   + str(self.get_height()) + " cm high.")

# Mutator methods
    def set_species(self, species):
        self.species = species

    def set_height(self, height):
        self.height = height

# Asseccor methods
    def get_species(self):
        return self.species

    def get_height(self):
        return self.height
# _________________________________________________________

# PlantWIthFlower subclass definition


class PlantWithFlowers(Plant):
    def __init__(self, species, height, common_name, color):
        Plant.__init__(self, species, height)
        self.common_name = common_name
        self.color = color
# Mutator methods

    def set_common_name(self, common_name):
        self.common_name = common_name

    def set_color(self, color):
        self.color = color

# Asseccor methods
    def get_common_name(self):
        return self.common_name

    def get_color(self):
        return self.color

# Str method for clear outputs

    def __str__(self):
        return str(self.get_species()  + ", commonly known as " 
                    + self.get_common_name() + " , is approximately "
                    + str(self.get_height()) + " cm high. The flowers are "
                    + self.get_color() + ".")

# _________________________________________________________

# PlantNoFlower subclass definition

class PlantNoFlowers(Plant):
    def __init__(self, species, height, reproduction):
        Plant.__init__(self, species, height)
        self.reproduction = reproduction
# Mutator methods

    def set_reproduction(self, reproduction):
        self.reproduction = reproduction

# Asseccor methods
    def get_reproduction(self):
        return self.reproduction


# Str method for clear outputs


    def __str__(self):
        return str(self.get_species() + " is approximately "
                   + str(self.get_height()) + " cm high and it reproduct by "
                   + self.get_reproduction())

# _________________________________________________________

# Roses subclass definition

class Roses(PlantWithFlowers):
    def __init__(self, species, height, common_name, color, number_of_pedals, thorns):
        PlantWithFlowers.__init__(self, species, height, common_name, color)

        self.number_of_pedals = number_of_pedals
        self.thorns = thorns

# Mutator methods
    def set_number_of_pedals(self, number_of_pedals):
        self.number_of_pedals = number_of_pedals

    def set_thorns(self, thorns):
        self.thorns = thorns

# Asseccor methods
    def get_number_of_pedals(self):
        return self.number_of_pedals

    def get_thorns(self):
        return self.thorns


# Str method for clear outputs

    def __str__(self):
        if self.get_thorns() == True:
            return str(self.get_species() + ", commonly known as "
                       + self.get_common_name() + " is approximately "
                       + str(self.get_height()) + " cm high, "
                       + self.get_color() + " rose species and it has "
                       + str(self.get_number_of_pedals()) 
                       + " pedals in one flower. "
                       + "It has thorns on it's stem.")
        else:
            return str(self.get_species() + ", commonly known as "
                       + self.get_common_name() + " is approximately "
                       + str(self.get_height()) + " cm high, "
                       + self.get_color() + " rose species and it has "
                       + str(self.get_number_of_pedals()) 
                       + " pedals in one flower. "
                       + "It hasn't thorns on it's stem.")

# _________________________________________________________

# FlowerShop subclass definition

class FlowerShop:
    def __init__(self, name, address, phone, selection):
        self.name = name
        self.address = address
        self.phone = phone
        self.selection = selection

# Mutator methods
    def set_name(self, name):
        self.name = name

    def set_address(self, address):
        self.address = address

    def set_phone(self, phone):
        self.phone = phone

    def set_selection(self, selection):
        self.selection = selection


# Asseccor methods

    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_phone(self):
        return self.phone

    def get_selection(self, list):
        print("They have in their selection flowers like: ")
        for i in list:
            print(i)


# Str method for clear outputs


    def __str__(self):
        return str(self.get_name() + "is a flower shop located in "
                   + self.get_address() + ". You can reach them by calling into number "
                   + self.get_phone())

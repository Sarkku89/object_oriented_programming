# File:  petClass.py
# Author: Sarianna Junnila
# Description:  Definitions for Animal and Pets classes

# Animal class definiton
class Animal:
    def __init__(self, species):

        self.species = species

# Str method
    def __str__(self):
        return str(self.get_species())

# Mutator methods 
    def set_species(self,species):
        self.species = species

# Asseccor methods
    def get_species(self):
        return self.species
#_________________________________________________________

# Pets subclass definition
class Pets(Animal):
    def __init__(self, owner, species, name):
        Animal.__init__(self,species)
        self.owner = owner
        self.name = name

# Mutator methods 
    def set_owner(self, owner):
        self.owner = owner
    def set_name(self, name):
        self.name = name

# Asseccor methods
    def get_name(self):
        return self.name
    def get_owner(self):
        return self.owner


# Str method for clear outputs
    def __str__(self):
        return str(self.get_species() + " "
        + self.get_name() + " is owned by "
        + str(self.get_owner()))


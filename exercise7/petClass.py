# File:  mammalObjet2.py
# Author: Sarianna Junnila
# Description:  The class for defining the 
#   mammals and the subclasses Cats and Dogs

# Mammal class definiton
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

# Cats subclass definition
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
        + self.get_owner() + " and it eats ")


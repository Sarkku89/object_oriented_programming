# File:   pwtClass.py
# Author: Sarianna Junnila
# Description:  Defining Animal and Pets classe.

class Animal:

    def __init__(self, species, size, weight):
        self.species = species
        self.size = size
        self.weight = weight

    def __str__(self):
        return str("\nMammal details:\n"+ "\nSpecies: " 
            + self.get_species() + "\nSize: " + self.get_size()
            + "\nWeight: " + self.get_weight())

# Mutator methods 

    def set_species(self,species):
        self.species = species

    def set_size(self,size):
        self.size = str(size)
    
    def set_weight(self,weight):
        self.weight = str(weight)

# Asseccor methods

    def get_species(self):
        return self.species
    
    def get_size(self):
        return self.size
    
    def get_weight(self):
        return self.weight

# Pets subclass definition
class Pets(Animal):
    def __init__(self, species, size, weight, owner, name):
        Animal.__init__(self,species, size, weight)
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
        + str(self.get_owner()) + ". It weigths "
        + str(self.get_weight()) + " kg and it's "
        + str(self.get_size()) + " cm in height.")


# File:  mammalObjet.py
# Author: Sarianna Junnila
# Description:  The class for defining the mammals

class Mammal:
    def __init__(self, species):

        self.species = species
    
    def __str__(self):
        return str(self.get_species())

# Mutator methods 

    def set_species(self,species):
        self.species = species
    

# Asseccor methods

    def get_species(self):
        return self.species
# File:  mammalObjet2.py
# Author: Sarianna Junnila
# Description:  The class for defining the 
#   mammals and the subclasses Cats and Dogs

# Mammal class definiton
class Mammal:
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
class Cats(Mammal):
    def __init__(self, noise, diet, owner, species, name):
        Mammal.__init__(self,species)
        self.noise = noise
        self.diet = diet
        self.owner = owner
        self.name = name

# Mutator methods 
    def set_noise(self, noise):
        self.noise = noise
    def set_diet(self, diet):
        self.diet = diet
    def set_owner(self, owner):
        self.owner = owner
    def set_name(self, name):
        self.name = name

# Asseccor methods
    def get_name(self):
        return self.name
    def get_diet(self):
        return self.diet
    def get_owner(self):
        return self.owner
    def get_noise(self):
        return self.noise

# Str method for clear outputs
    def __str__(self):
        return str(self.get_species() + " "
        + self.get_name() + " is owned by "
        + self.get_owner() + " and it eats " 
        + self.get_diet()+". It makes "
        + self.get_noise()+" noises.")

#_________________________________________

# Dogs subclass definition
class Dogs(Mammal):
    def __init__(self, noise, diet, owner, species, name):
        Mammal.__init__(self,species)
        self.noise = noise
        self.diet = diet
        self.owner = owner
        self.name = name

# Mutator methods 
    def set_noise(self, noise):
        self.noise = noise
    def set_diet(self, diet):
        self.diet = diet
    def set_owner(self, owner):
        self.owner = owner
    def set_name(self, name):
        self.name = name

# Asseccor methods
    def get_name(self):
        return self.name
    def get_diet(self):
        return self.diet
    def get_owner(self):
        return self.owner
    def get_noise(self):
        return self.noise

# Str method for clear outputs
    def __str__(self):
        return str(self.get_species() + " "
        + self.get_name() + " is owned by "
        + self.get_owner() + " and it eats " 
        + self.get_diet()+". It makes "
        + self.get_noise()+" noises.")
# File:  mammalObjet3.py
# Author: Sarianna Junnila
# Description:  Main class definition called Mammal and 
#   subclasses "DomesticAnimal", "WildAnimal", "Cats", "Dogs", "Giraffes and "Bears".

# Base class Mammal definiton

class Mammal:
    def __init__(self, species):

        self.species = species
    
    def __str__(self):
        return str("Mammal's species is" + self.get_species())

# Mutator methods 
    def set_species(self,species):
        self.species = species
    

# Asseccor methods
    def get_species(self):
        return self.species


# _______________________________________________________

# Subclass WildAnimal definition

class WildAnimal(Mammal):
    def __init__(self, species, when_active, continent):
        Mammal.__init__(self,species)
        self.when_active = when_active
        self.continent = continent

# Asseccor methods
    def get_when_active(self):
        return self.when_active
    def get_continent(self):
        return self.continent

# Mutator methods 
    def set_when_active(self, when_active):
        self.when_active = when_active
    def set_continent(self, continent):
        self.continent = continent

# Str method for clear outputs when printing the object
    def __str__(self):
        return str("Wild animal " + self.get_species()
            + " lives in " + self.get_continent() 
            + " and it's a " + self.get_when_active() 
            + " animal.")


# _______________________________________________________

# Subclass DomesticAnimal definition

class DomesticAnimal(Mammal):
    def __init__(self, species, owner, color, name):
        Mammal.__init__(self,species)
        self.owner = owner
        self.color = color
        self.name = name

# Asseccor methods
    def get_owner(self):
        return self.owner
    def get_name(self):
        return self.name

# Mutator methods 
    def set_owner(self, owner):
        self.owner = owner
    def set_name(self, name):
        self.name = name

# Str method for clear outputs when printing the object
    def __str__(self):
        return str("Domestic animal " + self.get_species() 
            + " is owned by "  + self.get_owner() 
            + " and it's name is "  + self.get_name())


# _______________________________________________________

# Subclass Cats definition

class Cats(DomesticAnimal):
    def __init__(self, species, owner, color, name, noise, diet):
        DomesticAnimal.__init__(self,species, owner, color, name)
        self.noise = noise
        self.diet = diet

# Mutator methods 
    def set_noise(self, noise):
        self.noise = noise
    def set_diet(self, diet):
        self.diet = diet

# Asseccor methods
    def get_diet(self):
        return self.diet
    def get_noise(self):
        return self.noise

# Str method for clear outputs when printing the object
    def __str__(self):
        return str(self.get_species() + " "
        + self.get_name() + " is owned by "
        + self.get_owner() + " and it eats " 
        + self.get_diet()+". It makes "
        + self.get_noise()+" noises. "
        + self.get_species() + " is a domestic animal.")


# _______________________________________________________

# Subclass Dogs definition

class Dogs(DomesticAnimal):
    def __init__(self, species, owner, color, name, noise, diet):
        DomesticAnimal.__init__(self,species, owner, color, name)
        self.noise = noise
        self.diet = diet

# Mutator methods 
    def set_noise(self, noise):
        self.noise = noise
    def set_diet(self, diet):
        self.diet = diet  

# Asseccor methods
    def get_diet(self):
        return self.diet
    def get_noise(self):
        return self.noise

# Str method for clear outputs when printing the object
    def __str__(self):
        return str(self.get_species() + " "
        + self.get_name() + " is owned by "
        + self.get_owner() + " and it eats " 
        + self.get_diet()+". It makes "
        + self.get_noise()+" noises. "
        + self.get_species() + " is a domestic animal.")


# _______________________________________________________

# Subclass Giraffes definition

class Giraffes(WildAnimal):
    def __init__(self, species, when_active, continent, height, weight, benefactor):
        WildAnimal.__init__(self,species, when_active, continent)
        self.height = height
        self.weight = weight
        self.benefactor = benefactor

# Mutator methods 
    def set_height(self, height):
        self.height = height
    def set_weight(self, weight):
        self.weight = weight
    def set_benefactor(self, benefactor):
        self.benefactor = benefactor

# Asseccor methods
    def get_height(self):
        return self.height
    def get_weight(self):
        return self.weight
    def get_benefactor(self):
        return self.benefactor

# Str method for clear outputs when printing the object
    def __str__(self):
        return str(self.get_species() + " is a "+ self.get_when_active() 
        +" wild animal and it lives in "+ self.get_continent() 
        + ". It weights " + str(self.get_weight())
        +" kg and it is " + str(self.get_height())+" cm high."
        + " This animal's benefactor is " + str(self.get_benefactor()))


# _______________________________________________________

# Subclass Bears definition

class Bears(WildAnimal):
    def __init__(self, species, when_active, continent, height, weight, benefactor):
        WildAnimal.__init__(self,species, when_active, continent)
        self.height = height
        self.weight = weight
        self.benefactor = benefactor

# Mutator methods 
    def set_height(self, height):
        self.height = height
    def set_weight(self, weight):
        self.weight = weight
    def set_benefactor(self, benefactor):
        self.benefactor = benefactor

# Asseccor methods
    def get_height(self):
        return self.height
    def get_weight(self):
        return self.weight
    def get_benefactor(self):
        return self.benefactor

# Str method for clear outputs when printing the object
    def __str__(self):
        return str(self.get_species() + " is a "+ self.get_when_active() 
        +" wild animal and it lives in "+ self.get_continent() 
        + ". It weights " + str(self.get_weight())
        +" kg and it is " + str(self.get_height())+" cm high."
        + " This animal's benefactor is " + str(self.get_benefactor()))
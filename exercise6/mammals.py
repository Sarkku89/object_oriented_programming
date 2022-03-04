""" Use the Mammal class (that you created in Exercise 4). 
Inherit species of animals from it(e.g. Dogs, Cats, etc.). 
Species of animals mean that you do not inherit an individual
animal, but the whole species (such as Dogs, Cats or Elephants). 
The individual animalsare then the individual objects. 
Add data attribute for the noise the species of animals
make and the diet they have and the animals name and owner. 
Create a few objects (=individual animals) from the inherited 
species and display them on screen (= Print outthe state of each object 
(use str-method))."""

import mammalObject2

class Cats(mammalObject2.Mammal):
    def __init__(self, noise, diet, owner, species, name):
        mammalObject2.Mammal.__init__(self,species)
        self.noise = noise
        self.diet = diet
        self.owner = owner
        self.name = name



    def set_noise(self, noise):
        self.noise = noise
    def set_diet(self, diet):
        self.diet = diet
    def set_owner(self, owner):
        self.owner = owner
    def set_noise(self,noise):
        self.noise = noise
    def set_name(self, name):
        self.name = name


    def get_name(self):
        return self.name
    def get_diet(self):
        return self.diet
    def get_owner(self):
        return self.owner
    def get_noise(self):
        return self.noise
    def get_name(self):
        return self.name


    def __str__(self):
        return str(self.get_species() + " "
        + self.get_name() + " is owned by "
        + self.get_owner() + " and it eats " 
        + self.get_diet()+". It makes "
        + self.get_noise()+" noises.")


class Dogs(mammalObject2.Mammal):
    def __init__(self, noise, diet, owner, species, name):
        mammalObject2.Mammal.__init__(self,species)
        self.noise = noise
        self.diet = diet
        self.owner = owner
        self.name = name



    def set_noise(self, noise):
        self.noise = noise
    def set_diet(self, diet):
        self.diet = diet
    def set_owner(self, owner):
        self.owner = owner
    def set_noise(self,noise):
        self.noise = noise
    def set_name(self, name):
        self.name = name


    def get_name(self):
        return self.name
    def get_diet(self):
        return self.diet
    def get_owner(self):
        return self.owner
    def get_noise(self):
        return self.noise
    def get_name(self):
        return self.name


    def __str__(self):
        return str(self.get_species() + " "
        + self.get_name() + " is owned by "
        + self.get_owner() + " and it eats " 
        + self.get_diet()+". It makes "
        + self.get_noise()+" noises.")
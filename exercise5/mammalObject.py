"""Create a mammal object. It has the following data attributes: ID, species, name, size and
weight. Roll the dice, based on the result check if the correct mammal (based on ID) fits
into your car’s trunk (that you created in previous task). Also check that your mammal 
does not exceed the car’s load limit. Give informative output prints and error 
messages."""

class Mammal:
    def __init__(self, id, species, name, size, weight):
        self.id = id
        self.species = species
        self.name = name
        self.size = size
        self.weight = weight
    
    def __str__(self):
        return str(self.get_species() + " called " + self.get_name()+ ". It is "
        + str(self.get_size())+" cm high and weights " + str(self.get_weight()) + " kg.\n")

# Mutator methods 

    def set_id(self,id):
        self.id = id

    def set_species(self,species):
        self.species = species
    
    def set_name(self,name):
        self.name = name
    
    def set_size(self,size):
        self.size = str(size)
    
    def set_weight(self,weight):
        self.weight = str(weight)

# Asseccor methods

    def get_id(self):
        return self.id

    def get_species(self):
        return self.species
    
    def get_name(self):
        return self.name
    
    def get_size(self):
        return self.size
    
    def get_weight(self):
        return self.weight

    def mammalLottery(self, dice_result):
        if dice_result <= 2:
            self.set_id (1)
            self.set_species("Guinea Pig")
            self.set_name("Squicky")
            self.set_size(15)
            self.set_weight(1)
        elif dice_result > 2 and dice_result <= 4:
            self.set_id (2)
            self.set_species("Cat")
            self.set_name("Kitty")
            self.set_size(45)
            self.set_weight(5)
        elif dice_result > 4 and dice_result <= 6:
            self.set_id (3)
            self.set_species("Dog")
            self.set_name("Blackie")
            self.set_size(60)
            self.set_weight(15)
        elif dice_result > 6 and dice_result <= 8:
            self.set_id (4)
            self.set_species("Donkey")
            self.set_name("George")
            self.set_size(150)
            self.set_weight(100)
        if dice_result > 8 and dice_result <= 10:
            self.set_id (5)
            self.set_species("Horse")
            self.set_name("Beauty")
            self.set_size(200)
            self.set_weight(55)
        elif dice_result > 10 and dice_result <= 12:
            self.set_id (6)
            self.set_species("Giraffe")
            self.set_name("Mr. Tall")
            self.set_size(480)
            self.set_weight(950)
        



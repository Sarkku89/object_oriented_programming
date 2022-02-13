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
        return str("\nMammal details:\n"+"ID: " + self.get_id() + "\nSpecies: " 
            + self.get_species() + "\nName: " + self.get_name() + "\nSize: " + self.get_size()
            + "\nWeight: " + self.get_weight())

# Mutator methods 

    def set_id(self,id):
        self.id = str(id)

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


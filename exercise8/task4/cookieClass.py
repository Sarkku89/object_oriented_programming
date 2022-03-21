# File:  cookieClass.py
# Author: Sarianna Junnila
# Description:  Defining cookie class

# Cookie class definiton

class Cookie:
    def __init__(self, baked, frozen, flavour):
        self.baked = baked
        self.frozen = frozen
        self.flavour = flavour

    # Mutator methods

    def set_baked(self, baked):
        self.baked = baked
    
    def set_frozen(self, frozen):
        self.frozen = frozen

    def set_flavour(self, flavour):
        self.flavour = flavour

    # Accessor method 
    def get_baked(self):
        if self.baked == True:
            return "baked"
        else:
            return "still raw"
    
    def get_frozen(self):
        if self.frozen == True:
            return "frozen"
        else:
            return "unfrozen"

    def get_flavour(self):
        return self.flavour
    
    # Str method for clear inputs
    
    def __str__(self):
        if self.get_flavour() == "":
            return str(
                "This cookie is "
                + self.get_baked()+ " and it is " + self.get_frozen())
        else:
            return str(
                "This "+self.get_flavour()+ " cookie is "
                + self.get_baked()+ " and it is " + self.get_frozen())
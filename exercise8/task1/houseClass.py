# File:  houseClass.py
# Author: Sarianna Junnila
# Description:  Defining house class

# Plant class definiton

class House:
    def __init__(self, windows, floors, bed, surfaces, fridge, toilet_paper):
        self.windows = windows
        self.floors = floors
        self.bed = bed
        self.surfaces = surfaces
        self.fridge = fridge
        self.toilet_paper = toilet_paper

    # Mutator methods

    def set_windows(self, windows):
        self.windows = windows
    
    def set_floors(self, floors):
        self.floors = floors

    def set_bed(self, bed):
        self.bed = bed

    def set_surfaces(self, surfaces):
        self.surfaces = surfaces

    def set_fridge(self, fridge):
        self.fridge = fridge

    def set_toilet_paper(self, toilet_paper):
        self.toilet_paper = toilet_paper

    # Accessor method 
    def get_windows(self):
        return self.windows
    
    def get_floors(self):
        return self.floors

    def get_bed(self):
        return self.bed
    
    def get_surfaces(self):
        return self.surfaces

    def get_fridge(self):
        return self.fridge
    
    def get_toilet_paper(self):
        return self.toilet_paper

    # Str method for clear inputs
    def __str__(self):
        return str(
        "The floors are "+ self.get_floors() +". "
        +"The windows are " + self.get_windows()+". "
        +"The surfaces are " + self.get_surfaces()+". "
        +"The bed is " + self.get_bed()+". "
        +"The fridge is " + self.get_fridge()+". "
        +"The toilet paper rack is " + self.get_toilet_paper()+". ")
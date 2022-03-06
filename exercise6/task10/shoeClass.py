# File:  shoeClass.py
# Author: Sarianna Junnila
# Description:  Defininf Shoes baseclass, subclasses for it (Sneakers, HikingBoots, 
#   Heels and SportingShoes) and sublcasses for SportingShoes(Skis, Skates)

# Shoes class definition
class Shoes:
    def __init__(self,size, material, color, laces, price, brand):
        self.size = size
        self.material = material
        self.color = color
        self.laces = laces
        self.price = price
        self.brand = brand

# Mutator methods 
    def set_size(self, size):
        self.size = size
    def set_material(self, material):
        self.material = material
    def set_color(self, color):
        self.color = color
    def set_laces(self, laces):
        self.laces = laces
    def set_price(self, price):
        self.price = price
    def set_brand(self, brand):
        self.brand = brand 

# Asseccor methods
    def get_size(self):
        return self.size
    def get_material(self):
        return self.material
    def get_color(self):
        return self.color
    def get_laces(self):
        if self.laces == True:
            return "Yes"
        else:
            return "No"
    def get_price(self):
        return self.price
    def get_brand(self):
        return self.brand

# Str method for clear outputs when printing the object
    def __str__(self):
        return str("Shoes:\n"+ "Brand: " + self.get_brand() 
            + "\nSize: " + str(self.get_size())
            + "\nMaterial: " + self.get_material()
            + "\nColor: " + self.get_color()
            + "\nLaces: " + self.get_laces()
            + "\nPrice: " + str(self.get_price()) + "€")
#___________________________________________________

# Sneaker subclass definition

class Sneaker(Shoes):
    def __init__(self, size, material, color, laces, price, brand, sole_thickness, style, intended_use):
        Shoes.__init__(self, size, material, color, laces, price, brand)
        self.sole_thickness = sole_thickness
        self.style = style
        self.intended_use = intended_use

# Asseccor methods
    def get_sole_thickness(self):
        return self.sole_thickness
    def get_style(self):
        return self.style
    def get_intended_use(self):
        return self.intended_use

# Mutator methods 
    def set_sole_thickness(self, sole_thickness):
        self.sole_thickness = sole_thickness
    def set_style(self,style):
        self.style = style
    def set_intended_use(self,intended_use):
        self.intended_use = intended_use
      
# Str method for clear outputs when printing the object
    def __str__(self):
        return str("Sneakers:\n"+ "Brand: " + self.get_brand() 
            + "\nSize: " + str(self.get_size())
            + "\nMaterial: " + self.get_material()
            + "\nColor: " + self.get_color()
            + "\nLaces: " + self.get_laces()
            + "\nPrice: " + str(self.get_price()) + "€"
            + "\nSole thickness: " + str(self.get_sole_thickness()) + " cm"
            + "\nStyle: " + self.get_style()
            + "\nIntended use: " + self.get_intended_use()
            )

#___________________________________________________

# HikingBoots subclass definition

class HikingBoots(Shoes):
    def __init__(self, size, material, color, laces, price, brand, pins, waterproof):
        Shoes.__init__(self,size, material, color, laces, price, brand)

        self.pins = pins
        self.waterproof = waterproof

# Asseccor methods
    def get_pins(self):
        if self.pins == True:
            return "Pins"
        else:
            return "No pins"

    def get_waterproof(self):
        if self.waterproof == True:
            return "Yes"
        else:
            return "No"

# Mutator methods 
    def set_pins(self, pins):
        self.pins = pins
    def set_waterproof(self, waterproof):
        self.waterproof = waterproof

# Str method for clear outputs when printing the object
    def __str__(self):
        return str("Hiking Books:\n"+ "Brand: " + self.get_brand() 
            + "\nSize: " + str(self.get_size())
            + "\nMaterial: " + self.get_material()
            + "\nColor: " + self.get_color()
            + "\nLaces:" + self.get_laces()
            + "\nPrice: " + str(self.get_price()) + "€"
            + "\nPins: " + self.get_pins()
            + "\nWaterproof: " + self.get_waterproof()
            )


#___________________________________________________

# Heels ubclass definition

class Heels(Shoes):
    def __init__(self, size, material, color, laces, price, brand, heel_height):
        Shoes.__init__(self,size, material, color, laces, price, brand)

        self.heel_height = heel_height

# Asseccor methods
    def get_heel_height(self):
        return self.heel_height

# Mutator methods 
    def set_heel_height(self, heel_height):
        self.heel_height = heel_height


# Str method for clear outputs when printing the object
    def __str__(self):
        return str("Heels:\n"+ "Brand: " + self.get_brand() 
            + "\nSize: " + str(self.get_size())
            + "\nMaterial: " + self.get_material()
            + "\nColor: " + self.get_color()
            + "\nLaces: " + self.get_laces()
            + "\nPrice: " + str(self.get_price()) + "€"
            + "\nHeel height: " + str(self.get_heel_height()) + " cm"

            )

#___________________________________________________

# SportingShoes subclass definition

class SportingShoes(Shoes):
    def __init__(self, size, material, color, laces, price, brand, sport):
        Shoes.__init__(self,size, material, color, laces, price, brand)

        self.sport = sport

# Asseccor methods
    def get_sport(self):
        return self.sport

# Mutator methods 
    def set_sport(self, sport):
        self.sport = sport


# Str method for clear outputs when printing the object
    def __str__(self):
        return str("Heels:\n"+ "Brand: " + self.get_brand() 
            + "\nSize: " + str(self.get_size())
            + "\nMaterial: " + self.get_material()
            + "\nColor: " + self.get_color()
            + "\nLaces: " + self.get_laces()
            + "\nPrice: " + str(self.get_price()) + "€"
            + "\nSport: " + str(self.get_sport()))


#___________________________________________________

#___________________________________________________

# Definition for SportingShoes subclasses SkiBoots and Skates

class SkiBoots(SportingShoes):
    def __init__(self, size, material, color, laces, price, brand, sport, fastening_type, type_of_ski):
        SportingShoes.__init__(self,size, material, color, laces, price, brand, sport)

        self.fastening_type = fastening_type
        self.type_of_ski = type_of_ski

# Asseccor methods
    def get_fastening_type(self):
        return self.fastening_type
    def get_type_of_ski(self):
        return self.type_of_ski

# Mutator methods 
    def set_fastening_type(self, fastening_type):
        self.fastening_type = fastening_type
    def set_type_of_ski(self, type_of_ski):
        self.type_of_ski = type_of_ski


# Str method for clear outputs when printing the object
    def __str__(self):
        return str("Heels:\n"+ "Brand: " + self.get_brand() 
            + "\nSize: " + str(self.get_size())
            + "\nMaterial: " + self.get_material()
            + "\nColor: " + self.get_color()
            + "\nLaces: " + self.get_laces()
            + "\nPrice: " + str(self.get_price()) + "€"
            + "\nSport: " + str(self.get_sport())
            + "\nFastening type: " + self.get_fastening_type()
            + "\nType of ski: " + self.get_type_of_ski()

            )


class Skates(SportingShoes):
    def __init__(self, size, material, color, laces, price, brand, sport, figure, icehokey, blade_len, blade_hei ):
        SportingShoes.__init__(self,size, material, color, laces, price, brand, sport)

        self.figure = figure
        self.icehokey = icehokey
        self.blade_len = blade_len
        self.blade_hei = blade_hei

# Asseccor methods
    def get_figure(self):
        if self.figure == True:
            return "Yes"
        else: 
            return "No"
    def get_icehokey(self):
        if self.icehokey == True:
            return "Yes"
        else: 
            return "No"
    def get_blade_len(self):
        return self.blade_len
    def get_blade_hei(self):
        return self.blade_hei

# Mutator methods 
    def set_figure(self, figure):
        self.figure = figure
    def set_icehokey(self, icehokey):
        self.icehokey = icehokey
    def set_blade_len(self, blade_len):
        self.blade_len = blade_len
    def set_blade_hei(self, blade_hei):
        self.blade_hei = blade_hei


# Str method for clear outputs when printing the object
    def __str__(self):
        return str("Heels:\n"+ "Brand: " + self.get_brand() 
            + "\nSize: " + str(self.get_size())
            + "\nMaterial: " + self.get_material()
            + "\nColor: " + self.get_color()
            + "\nLaces: " + self.get_laces()
            + "\nPrice: " + str(self.get_price()) + "€"
            + "\nSport: " + str(self.get_sport())
            + "\nFigure Skates: " + self.get_figure()
            + "\nIcehokey skates: " + self.get_icehokey()
            + "\nBlade lenght: " + str(self.get_blade_len()) + " cm"
            + "\nBlade height: " + str(self.get_blade_hei()) + " cm"
            )


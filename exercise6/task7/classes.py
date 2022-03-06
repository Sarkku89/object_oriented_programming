# File:  classes.py
# Author: Sarianna Junnila
# Description:  Classes for Participants of Object Oriented Class, 
#   subclasses for Students and Teachers

# OOPParitcipants class definition
class OopParticipants:
    def __init__(self, start_month, end_month, year, prog_lang, name, wild, domestic):
        self.start_month = start_month
        self.end_month = end_month
        self.year = year
        self.prog_lang = prog_lang
        self.name = name
        self.wild = wild
        self.domestic = domestic

# Mutator methods 
    def set_start_month(self, start_month):
        self.start_month = start_month
    def set_end_month(self, end_month):
        self.end_month = end_month
    def set_year(self, year):
        self.year = year
    def set_prog_lang(self, prog_lang):
        self.prog_lang = prog_lang
    def set_name(self, name):
        self.name = name
    def set_wild(self,wild):
        self.wild = wild
    def set_domestic(self, domestic):
        self.domestic = domestic

# Asseccor methods
    def get_start_month(self):
        return self.start_month
    def get_end_month(self):
        return self.end_month
    def get_year(self):
        return self.year
    def get_prog_lang(self):
        return self.prog_lang
    def get_name(self):
        return self.name
    def get_wild(self):
        return self.wild
    def get_domestic(self):
        return self.domestic

# Str method for clear outputs when printing the object
    def __str__(self):
        return str(self.get_name() + "takes part into a OOP course between " 
            + self.get_start_month() + " and " 
            + self.get_end_month() + str(self.get_year))

#___________________________________________________

# Stundent subclass definition

class Student(OopParticipants):
    def __init__(self, start_month, end_month, year, prog_lang, name, wild, domestic, student_id, grade):
        OopParticipants.__init__(self,start_month, end_month, year, prog_lang, name, wild, domestic)

        self.student_id = student_id
        self.grade = grade

# Asseccor methods
    def get_student_id(self):
        return self.student_id
    def get_grade(self):
        return self.grade

# Mutator methods 
    def set_student_id(self, student_id):
        self.student_id = student_id
    def set_grade(self, grade):
        self.grade = grade

# Str method for clear outputs when printing the object
    def __str__(self):
        return str(self.get_name()+ " (id: " + str(self.get_student_id())+ ") "
            + " took part into a OOP course between " + self.get_start_month() 
            + " and " + self.get_end_month() + " " +str(self.get_year()) + ".\n"
            + "On the course he/she used " + self.get_prog_lang()
            + " to program. His/Her grade was " + str(self.get_grade())
            + ".\nShe/he owns these animals " + ', '.join(set(self.get_domestic())) 
            + " and is a benefactor for a " +  ', '.join(set(self.get_wild())))

#___________________________________________________

# Teacher subclass definition

class Teacher(OopParticipants):
    def __init__(self, start_month, end_month, year, prog_lang, name, wild, domestic, number_of_students, number_of_courses):
        OopParticipants.__init__(self, start_month, end_month, year, prog_lang, name, wild, domestic)

        self.number_of_students = number_of_students
        self.number_of_courses = number_of_courses

# Asseccor methods
    def get_number_of_students(self):
        return self.number_of_students
    def get_number_of_courses(self):
        return self.number_of_courses

# Mutator methods 
    def set_number_of_students(self, number_of_students):
        self.number_of_students = number_of_students
    def set_number_of_courses(self, number_of_courses):
        self.number_of_courses = number_of_courses

# Str method for clear outputs when printing the object
    def __str__(self):
        return str("Teacher " + self.get_name()
        + " teaches currently on" + str(self.get_number_of_courses())
        + " courses and " + str(self.get_number_of_students())
        + " students.\nOne of the courses is OOP course with " + self.get_prog_lang()
        + "." + "It started " + self.get_start_month() 
        + " and it ends in " + self.get_end_month()+ " " + str(self.get_year() )
        + ".\nShe/he owns these animals " + ', '.join(set(self.get_domestic())) 
        + " and is a benefactor for a " +  ', '.join(set(self.get_wild())) )

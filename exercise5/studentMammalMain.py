"""5.Create a class called Student and use the following data attributes:
first name, last name and student id. Remember to code accessor 
and mutator methods and str-method. Store students and their pet mammal 
to dictionary (use the mammals from Exercise 4). Think, what should 
be used as the dictionary key. Code a function that prints out 
each student and their mammal’s information. 
Use informative and clear output print.
6.Let the student select his/her pet mammal by rolling 2 dices 
and using their sum to indicate a correct mammal. The higher the number, 
the heavier mammal you get as your pet. (2 points)"""
import mammalObject
import studenClass

def printing_info(dictionary):
    for key in dictionary:
        print ("Student", key, "has a", dictionary[key])
        

def main():
    mammal = mammalObject.Mammal(
        id = "1",
        species = "Dog",
        name = "Blackie",
        size = 60,
        weight= 15
    )

    mammal2 = mammalObject.Mammal(
        id = "2",
        species = "Cat",
        name = "Kitty",
        size = 45,
        weight= 5
    )
    
    student = studenClass.Student(
        first_name= "Tamara",
        last_name= "Jones",
        student_id= 1)

    student2 = studenClass.Student(
        first_name= "Tommy",
        last_name= "Davis",
        student_id= 2    )

    student_list= [student, student2]

    dictionary = {
        student : mammal,
        student2 : mammal2
    }

    printing_info(dictionary)


main()




"""speciess = ["Dog", "Cat", "Horse", "Guinea Pig", "Giraffe", "Donkey"]
    names = ["Blackie", "Kitty", "Beauty", "Squicky", "Mr. Tall", "Geogre"]
    sizes = [60, 45, 200, 15, 480, 150]
    weights = [15, 5, 550, 1, 950, 100]"""
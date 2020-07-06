# The super class, Student is the class that other classes inherits from
class Student:
    # method (behaviour) initialises the variables
    def __init__(self, name, age, course): # (name, age, course attributes are defined)
        self.name = name
        self.__age = age
        self.course = course

    # Details of the student
    def details(self):
        # basic print functions
        print("Name: " + self.name)
        print("Age: " + self.__age)
        print("University course: " + self.course)

    def graduate(self):
        print("I graduated from university recently")
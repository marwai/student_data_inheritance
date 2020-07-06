# Imports everything (*) from student_data
from student_data import *

# The subclass devops has student as its base class
class Devops(Student): # The class inherits all the characteristics from student_data
    def __init__(self, name, age, course, skills):
        super().__init__(name, age, course)
        self.skills = skills # unique to devops only





#Recalls the instance of the class

# instance of method has been named from Devops
b =  Devops("bob", "25", "Computer Science", "SQL, Python and AWS\n")
# instance of Student
a = Student("bob", "25", "Computer Science")

#Both produce the same output due to inheritance
a.details()
a.graduate()
print("___")
b.details()
b.graduate()

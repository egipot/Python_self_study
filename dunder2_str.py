#__str__()
#@python programming FB  @dynamic.coding

#Magic Methods in Python

#This method helps us to display the object according to our requirements.
# The print function displays the memory location of the object, but if we want to modify, we can do this by using __str__() function

class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
    def __str__(self):
        return ('{} {}'.format(self.name, self.roll_no))
    
stud_1 = Student("Anna", 1)

print(stud_1)

#output
#Anna 1

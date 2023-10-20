#__sizeof__()
#@python programming FB  @dynamic.coding

#Magic Methods in Python

#If we want to know the memory allocated to that object, then we can call of override the __sizeof__() function and pass our object

class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

stud_1 = Student ('Anne', 1)
print('Size of student class object', stud_1.__sizeof__())

list_1 = [1, 2, 3, 4]
tuple_1 = (1, 2, 3, 4, 5)
dict_1 = {'a':1, 'b':2, 'c':3, 'd':4}

print('Size of list_1: ', list_1.__sizeof__())
print('Size of tuple_1: ', tuple_1.__sizeof__())
print('Size of dict_1: ', dict_1.__sizeof__())


#Output
# Size of student class object 32
# Size of list_1:  104
# Size of tuple_1:  64
# Size of dict_1:  216
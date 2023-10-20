#__new__()
#@python programming FB  @dynamic.coding

#Magic Methods in Python

#This method helps the constructor __init__() method to create objects for a class.
#So when we create an instance of a class, the Python interpreter first calls the __new__() method and after that __init__() method

class Sample:
    def __new__ (self, parameter):
        print("new invoked", parameter)
        return super().__new__(self)
    def __init__(self, parameter):
        print("init invoked", parameter)

obj = Sample ('a')

# Output:
# new invoked a 
# init invoked a

#__new__()
#@python programming FB  @dynamic.coding

#Magic Methods in Python

#How do we check what are the dunder (double underscore) and how many of them are in the standard class?
# 1. Create a sample class
# 2. Create its object
# 3. Use the dir() function and insert the object inside it. print(dir(obj))
# 4. This function prints a list of all the Magic Methods along with data members and member functions that are assigned to the class


class Sample:
    pass

print(dir(Sample))

#Output:
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', 
#  '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', 
#  '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', 
#  '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
#  '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
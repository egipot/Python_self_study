#Use the Python reduce() function to reduce a list into a single value.


from functools import reduce

numbers = [1,2,3,4,5]
product = reduce(lambda x, y: x*y, numbers)
#reduce(function, iterable, initializer=None/optional)
print(product)

#120
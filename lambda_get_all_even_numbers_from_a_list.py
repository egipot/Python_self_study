numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = filter(lambda x: x%2 == 0, numbers)
print(list(even_numbers))

#[2, 4, 6, 8, 10]
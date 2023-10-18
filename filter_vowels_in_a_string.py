#filter the vowels in the string

# https://www.programiz.com/python-programming/methods/built-in/filter

string = input("Please enter a string: ")

# a function that returns True if letter is vowel
def filter_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return True if letter in vowels else False

filtered_vowels = filter(filter_vowels, string)

# converting to tuple
vowels_tuple = tuple(filtered_vowels)
vowels_set = set(filtered_vowels)
vowels_list = list(filtered_vowels)
print(vowels_tuple)
print(vowels_set)
print(vowels_list)
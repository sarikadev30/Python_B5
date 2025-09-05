countries = ["India", "France", "Japan", "Canada"]
capitals = ["New Delhi", "Paris", "Tokyo", "Ottawa"]

CCD = {}
for i in range(len(countries)):
    CCD[countries[i]] = capitals[i]

print(CCD)
# x = input("Enter a country name : ")
# print(CCD[x])

# ...............................................................
# CRUD => C R U

# DELETE

# pop => delete a key-value pair based on key
# CCD.pop("Japan")
# print(CCD)
# ............................................
# popitem => remove the last key-value pair
# CCD.popitem()
# print(CCD)
# ............................................
# clear => remove all the key-value pairs
# CCD.clear()
# print(CCD)
# ............................................
# del => deletes the dictionary
# del CCD
# print(CCD)
# ...............................................................
# Functions/Methods in dictionary

# get => get the value based on keys . Also add customize msg when key is not there
# print(CCD["Japan"])
# print(CCD["S"])
# print(CCD.get("S", "Not Found"))
# ............................................
# keys => to get all the keys
# print(CCD.keys())
# ............................................
# values => to get all the values
# print(CCD.values())
# ............................................
# items => to get all the key-value pairs
# print(CCD.items())

# for key, val in CCD.items():
#     print(key, val)
# .....................................................................
"""
Problem 1
You have the following set:
words = {"hello", "world", "python", "programming", "sets"}

- a. Remove all words that have more than 5 letters using a loop.
- b. Add the word `"code"` to the set.
- c. Display the final set.
"""

numbers = {"a": 10, "b": 15, "c": 5, "d": 20}
threshold = 12

"""
Problem 2
Count Vowels in a String
Write a program to count the number of each vowel in a given string and store the counts in a dictionary.
string = "hello world"
Output: {'a': 0, 'e': 1, 'i': 0, 'o': 2, 'u': 0}
"""
# .................................................................

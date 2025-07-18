# Convert the following into valid multi-word variable names:

# total_marks_of_student=5687
# isstudent_present_today=True
# Average_Score=89

# xam-ty=78
# ...........................................................................
# Type Checking => type()

# a = 34
# b = 45.0
# c = True
# d = "Sam"

# print(type(c))
# print(type(b))
# print(type(a))
# print(type(d))
# .............................................................................
"""
name
age
city
"""
# .............................................................................
name = "Sam"
age = 23
city = "NewYork"
print(name, age, city)
# Formated String
# My name is Sam. I am 23 year old . I live in NewYork
# .............................................................................

# Formated String
# price=90
print(f"My name is {name}. I am {age} year old . I live in {city}")
# print(f"Total value of Product A: ${price}")
#
# .............................................................................

# DATA TYPES

# Bottle

# Basket

# int =>
# float
# str
# bool

# a = 34
# b = 45.0
# c = True
# d = "Sam"

# print(c, type(c))
# print(b, type(b))
# print(a, type(a))
# print(d, type(d))

# ........................................................
# Type Casting

# Implicit
# x = 23
# print(x)
# print(type(x))

# x = "Sam"
# print(x)
# print(type(x))

# Explicit

# int() => change the data type to Integer
# string => int
# float => int
# bool => int
# y = "12"
# y = 34.90
# y = False
# print(int(y), type(int(y)))

# str() => change to string data type
# y = True  # => y="34"   y="True"
# print(str(y), type(str(y)))

# float() => change to float data type
# z=24
# z = "34"
# z = False
# print(float(z), type(float(z)))


# bool() => changes to boolean data type
# z = "tyvhbnjbjnjk"  # empty string give False
# print(bool(z), type(bool(z)))

# z = 0
# print(bool(z), type(bool(z)))

# ...............................................................................
# Assigning one value to multiple variables
# a = 34
# b = 34
# c = 34
# d = 34

# print(a, b, c, d)

# a = b = c = d = 34
# print(a, b, c, d)

# Assigning Multiple values to multiple variable
# a = 34
# b = 56
# c = 67
# d = 12

# print(a, b, c, d)

# a, b, c, d = 34, 56, 67, 12
# print(a, b, c, d)
# .......................................................................

# Input taking  => input()

# x = 45
# y = 67
# z = input("Enter a number: ")
# print(z, type(z))
# z = int(z)
# print(z, type(z))

# .........................................................................................................
#  Take the output from the user and it needs to be a number and then Add 5 to it and print that number

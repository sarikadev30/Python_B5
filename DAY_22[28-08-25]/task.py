# even_numbers = {2, 4, 6, 8, 10}
# prime_numbers = {2, 3, 5, 7}

# x = even_numbers & prime_numbers
# print(x)
# even_numbers = even_numbers - x
# print(even_numbers)
# ...................................................................
# TUPLE

# CRUD => CREATE ,  READ ,  UPDATE=> X ,  DELETE => X
# CREATE
# x = (1, 2, "Sam", "Joe", 34.09, True)
#    0  1   2       3     4       5
# print(x, type(x))
# Error => AttributeError: 'tuple' object has no attribute 'append'
# x.append("Monica")
# print(x)

# READ =>
# Indexing
# print(x[3])
# print(x[5])
# x = (2, 3, 5, 6, 7, 8, 9, 10)
#    0  1  2  3  4  5  6   7
# for i in x:
#     print(i + 4)

# Slicing
# x[start:end:step]
# print(x[0:5:1])
# print(x[:5:1])
# print(x[:5:])
# print(x[3::])  # print all elements from index 3
# print(x[::])

# x = (2, 3, 5, 6, 7, 8, 9, 10)
#    0  1  2  3  4  5  6   7
#    -8 -7 -6 -5 -4 -3 -2 -1
# print(x[-3])
# print(x[5:0:-1])
# print(x[-3:-7:-1])

# Merging
# y = (12, 13, 14, 15, 16, 17)
# # z = x + y
# z = y + x
# print(z)

# Another way of Creating a tuple
# c = tuple([121, 223, 122, 123, 324, 345])
# print(c, type(c))

# Tuple => List => make the changes => Change it to tuple
# newList = list(c)
# # print(newList, type(newList))
# newList[2] = 120
# # print(newList)
# newTuple = tuple(newList)
# print(newTuple)

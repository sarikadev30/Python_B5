# y = [1, 2, 3, 4, 5, 6, 7]
# print(y[2:6:1])
# ......................................................................
# SETS
# x = {1, 2, 3, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5}
# print(x, type(x))

# c = x[1:4:1]
# print(c)

# CRUD => CREATE READ UPDATE (Add) DELETE
# CREATE
# Way-1
# y = {1, 2, 3, 4, 4}
# Way-2
# z = set((3, 2, 4, 1, 2))
# print(z, type(z))

# READ
# for i in z:
#     print(i, end=", ")

# UPDATE
# add
# z = set((3, 2, 4, 1, 2))
# add single element
# z.add(9)
# print(z, type(z))
# z.add(3)
# print(z, type(z))

# add List
# a = [10, 23, 45, 123, 5]
# z.update(a)
# print(z, type(z))

# DELETE
# remove => if value is not available in the set, it will raise the error
# z.remove(2)
# print(z)
# z.remove(8)
# print(z)

# discard => if value is not available in the set, it will not raise the error
# z.discard(3)
# print(z)
# z.discard(8)
# print(z)

# clear => to remove all the elements from the set (to empty the set)
# z.clear()
# print(z)

# Searching
# print(3 in z)
# print(10 in z)

# ....................................................................................
letters = set("mississippi")
print(letters, len(letters))
letters.pop()  # first element from the set
print(letters)

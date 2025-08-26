"""
....*
...***
..*****
.*******
*********
 *******
  *****
   ***
    *
"""

# i= rows
# j=cols
# k=spaces
# i=1  j=1  k=4   k=(n-i)       j=(2*i-1)   i=4 j=8-1=7
# i=2  j=3  k=3
# i=3  j=5  k=2
# i=4  j=7  k=1
# i=5  j=9  k=0
# n = 5
# for i in range(n, 0, -1):
#     # k=> for spaces
#     for k in range(n - i):
#         print(" ", end="")
#     # j=> for *
#     for j in range(2 * i - 1):
#         print("*", end="")
#     print()

# ....................................................................................

# DATA TYPES => int float str bool
# Data Types =>
# Primitive Data Type => int float str bool
# These are immutable
# x = "earn"
# x[1] = "b"
# Non Primitive Data Type => list tuple set dictionary
# These are mutable
# y = [1, "multiple", 34, True, 34.90]
# print(y)
# y[2] = 43
# print(y)

# ................................................................................
# LIST => store multiple values (CRUD=> Operation C=Create R=Read U=Update D=Delete)

# CREATE
# z = [1, 2, 3, 4, "Sam", 3.4, True, False, 54.90]
# #   0  1  2  3   4     5     6     7      8
# #  -9 -8 -7 -6  -5    -4    -3    -2      -1
# print(z, type(z))
# print(len(z))

# READ
# Indexing =>
# Positive Indexing => 0-(n-1) (left to right)
# Negative Indexing => -(n)- (-1) (right to left)
# print(z[4])
# print(z[-2])

# K = [1, 2, 3, "Sam", "Danny", True, 3.4, [1, 4, 5, 6, 7]]

# print(K[-1][1])
# print(K[-3])

# # Loops
# z = [1, 2, 3, 4, "Sam", 3.4, True, False, 54.90]

# for i in z:
#     print(i)

# for i in range(len(z)):
#     print(i, z[i])


# Slicing =>

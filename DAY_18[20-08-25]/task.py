# K = [1, 2, 3, "Sam", "Danny", True, 3.4, [1, 4, 5, 6, 7]]

# # +ve Indixing 0 => n-1
# #  -ve Indexing -1 => -n (right to left)
# # READ
# print(K[-2])  # 3.4
# print(K[7][-2])  # 3.4 3.4      # 6
# print(K[-4])  # Danny

# ..........................................................................
# SLICING

# z = [2, 3, 4, 1, 6, 7, 8, 9, 10, 23]
#    0  1  2  3  4  5  6  7   8   9

# listName[startIndex: EndIndex+1:Step]   (start,end,step)

# print(z[2:6:1])
# print(z[:3:2])  # start default => 0
# print(z[:5:])  # step default => 1

# print(z[6::-1])  # end not given : goes upto end
# print(z[-1:-4:-1])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

# print(thislist[-4:-1])
# print(thislist[:4])
# print(thislist[2:5])
# print(thislist[2:])

# ......................................................................................
# UPDATE  => Replace any thing => AddSomething

z = [2, 3, 4, 1, 6, 7, 8, 9, 10, 23]
#    0  1  2  3  4  5  6  7   8   9

# REPLACE
# print(z)
# z[4] = -12
# z[-2] = -10
# print(z)

# ADDITION
#  APPEND: adding an element => add at the end
# z.append(123456)
# print(z)

# INSERT : add the element at particular index  =>insert(position, value)
# z.insert(7, 345)
# print(z)

# INSERT AND APPEND FOR LIST
# z = [2, 3, 4, 1, 6, 7, 8, 9, 10, 23]
#    0  1  2  3  4  5  6  7   8   9

# z.append([12, 13, 14])
# print(z)

# z.insert(-2, [12, 13, 14])
# print(z)

#  EXTEND: adding list elements => at the end
# print(z)
# y = ["Hi", "Bye", "SAM"]
# z.extend(y)
# # z.append(y)
# print(z)
# ..............................................................

# PROBLEM 1 **Perform the following tasks :**
# 1. **Create list of superheroes**
# 2. **push 4 superheroes in the List**
# 3. **Print the List**
# sup = ["Ironman"]

# ...............................................................
# DELETE
# z = [2, 3, 4, 1, 6, 7, 8, 9, 10, 23, 10, 10, 10, 10, 10]
#    0  1  2  3  4  5  6  7   8   9
# POP: Using an Index
# print(z)
# print(z.pop(2))
# print(z)

# REMOVE : Delete using Value
# If multiple values are there => it will remove the first iteration
# z.remove(10)
# print(z)
# ..........................................................................

# stationary = []
# stationary.extend(["pen", "pencil", "notebooks", "marker", "Eraser", "Sharpner"])
# print(stationary)
# stationary.remove("marker")
# print(stationary)
# stationary.pop(2)
# print(stationary)
# stationary.pop()
# print(stationary)

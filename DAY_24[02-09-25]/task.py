# DICTIONARY

# d = {"name": "Sam", "age": 22, "city": "NewYork"}
# print(d, type(d))
# duplicate keys not allowed
# d = {"name": "Sam", "age": 22, "city": "NewYork", "name": "Joe", "age": 12}
# print(d, type(d))
# print(d["city"])
# .....................................................................................
# CRUD =>

# CREATE
# 1.
d = {"name": "Sam", "age": 22, "city": "NewYork"}
# 2.
x = dict({"a": 4, "b": 2, "c": 45, "d": 56})
# print(x, type(x))
# ......................................................................................
# READ
# print(d["age"])
# print(len(d), len(x))

# loop
# for i in d:
#     print(i, d[i])

# d = {
#     "name": ["Anny", "Bunny", "Danny", "Enav"],
#     "age": [25, 36, 22, 32],
#     "income": [90, 75, 80, 93],
# }
# print(f"{d["name"][0]} - {d["age"][0]}")
# print(f"{d["name"][0]} - {d["age"][0]} - {d["income"][0]}")

# for i in d:
#     print(i, d[i][2])
# ...........................................................................
# UPDATE
d = {"name": "Sam", "age": 22, "city": "NewYork"}

# replace value
# d["name"] = "Monica"
# print(d)
# add a new-key value pair
# d["salary"] = 45000
# print(d)
# Keys are unique value can be duplicated
# ...........................................................................
# DELETE

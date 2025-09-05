# Problem 4
# numbers = {"a": 10, "b": 15, "c": 5, "d": 20}
# threshold = 12
# dec = {}
# for i in numbers.keys():
#     if numbers[i] < threshold:
#         dec[i] = numbers[i]
# print(dec)

# .................................................................
# Functions


# def func():
#     print("Hello World!...")


# func()


# def add():
#     x = 23
#     b = 10
#     print(x + b)


# add()
# add()
# add()


# def addF(a, b):
#     print(a + b)


# addF(4, 3)
# addF(14, 3)
# addF(10, 13)


# def mulFun(x, y, z):
#     print(x * y * z)


# mulFun(2, 3, 4)

# ............................................................................
# Different types of arguments
# default argument


def subtract(x=1, y=1):
    print(x - y)


subtract(3, 2)
subtract(3)
subtract()

# make a function mulFun and print the product of 3 arguments and take a default value as 1 for any one argument

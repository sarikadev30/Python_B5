# Make a function that takes 2 arguments fName and lName and then print the full name of the person.
# Make lName as default argument
# TYPES OF ARGUMENTS => 1. default  2. Variable-Length 3. Keyworded
# ......................................................................
# DEFAULT ARGUMENT
# def fullNameFun(fName, lName="Jordan"):
#     print(f"{fName}-{lName}")

# fullNameFun("Sam", "Roy")
# fullNameFun("Sam")
# .......................................................................
# VARIABLE-LENGTH ARGUMENTS
# def addFun(*t):
#     print(t)
#     val = sum(t)
#     print(val)

# addFun(2, 3, 4, 5, 6, 7, 8, 9, 2)
# addFun(2, 3, 4)
# addFun(2)
# addFun(2, 78, 1, 0)
# .......................................................................
# KEYWORDED ARGUMENTS

# def studentDetails(name, age, city):
#     print(f"name => {name} \nage => {age} \ncity=> {city}")

# studentDetails("Joe", 23, "NY")
# studentDetails("Joe", city="NY", age=34)
# studentDetails(city="NY", age=38, name="Monica")

# ........................................................................
# DIFFERENCE BETWEEN PRINT AND RETURN


# def calBatch(x, y, z):
#     val = x * y * z
#     print(val)


# calBatch(9, 8, 1)


# def calBatchR(x, y, z):
#     val = x * y * z
#     return val


# print(calBatchR(9, 8, 1))


# x = calBatchR(9, 8, 1)
# print(x)

# ...........................................................

# Factorial of a number

# 5 => 5! => 5*4*3*2*1 => 120
# 3 => 3! => 3*2*1 => 6
# 2 => 2! => 2*1 => 2
# 0 => 0! => 1


# def fact(n):
#     f = 1
#     for i in range(n, 0, -1):
#         f = f * i

#     print(f)


# fact(5)
# fact(3)
# ...............................................................
# Fibonacci Series

# next value= sum of previous two values

# 0 1 1 2 3 5 8

# def fib(n):

# fib(n)

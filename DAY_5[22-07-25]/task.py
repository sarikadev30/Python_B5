# Logical Operators
# And  => All expressions should return True
# print(True and False)
# print(False and False)
# print(False and True)
# print(True and True)

# x = 6 > -2
# y = 56 > 0
# print(x and y)

# OR => Any one value needs to be true
# print(True or False)
# print(False or False)
# print(False or True)
# print(True or True)

# x = 6 < -2
# y = 56 < 0
# print(x or y)

# NOT => It negates the expression value / It gives opposite of it
# print(not True)
# print(not False)

# x = 5 == 4
# print(not x)
# ..................................................................
# Problems :

# a = 9 < 11       # T
# b = 2 == 3       # F
# c = 10 > 3       # T
# result = a and (b or c)
# print(result)  # True #True
# .................................................................

# x = 4 <= 4   # T
# y = 10 < 5   # F
# z = not (x and y)
# print(z)  # True  # True


# .................................................................

# m = 0 != 0      #F
# n = 1 == 1      #T
# o = m and not n
# print(o)  # False


# .................................................................

# p = 6 == 6
# q = 5 != 5
# r = not (p or q)
# print(r)

# .................................................................

# p = 10 < 5  # F
# q = 3 == 3  # T
# r = 7 != 7  # F
# result = not (p or q and r)  # T and F
# print(result)
# .............................................................

# Check The number positive
# x = -12
# print(x > 0)

# Check the number negative
# y = -23
# print(x < 0)
# print(x <= -1)

# Integer  => Positive  or Negative or Zero
# .............................................................
# Check the Number is Even
# x = 92
# print(x % 2 == 0)

# 3%2 => 1  4%2 => 0  5%2=> 1 6%2=> 0

#  Check the Number is Odd
# print(x % 2 != 0)
# print(x % 2 == 1)
# .............................................................
# Check the number is divisible by 3
x = 93
# %2 => 0 1
# %3 => 0 1 2
# 1 % 3 = 1
# 2 % 3 = 2
# 3% 3=0
# 4%3=1
# 5%3=2
# 6%3=0
# 7%3=1
# 8%3=2
# %4 => 0 1 2 3
# print(x % 3 == 0)

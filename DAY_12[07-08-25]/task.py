# Sum of digits
# n=1234
# sum=1+2+3+4 => 10

# 1st way :
# n = 1234
# x = str(n)
# # print(n, x, type(n), type(x))
# i = len(x) - 1
# # print(len(x)) 3 2 1 0
# sum = 0
# while i >= 0:
#     sum += int(x[i])
#     i -= 1

# print(sum, type(sum))
# ...........................................................
# 2nd way :
n = 7683
# 1234 // 10
# 1234 % 10
#  123 sum=4
#  12  sum=4+3=7
#  1  sum=7+2=9
#  0  sum= 9+1=10

# a = n
# sum = 0
# while a > 0:
#     r = a % 10
#     print(r)
#     sum += r
#     a = a // 10
# print(sum)
# ..................................................................
# FOR LOOP

# for i in sequence:
# print(i)

# range (start, end ,step)

# for i in range(1, 5, 1):  # 1 2 3 4
#     print(i)

# Step by default value = 1
# for i in range(1, 5):
#     print(i)

# start by default value = 0
# for i in range(5):
#     print(i)

# for i in range(5, 0, -1):
#     print(i)

# for i in range(5, -1, -1):
#     print(i)

# for i in range(0, 10, 3):
#     print(i)

# ..............................................................
#  to print numbers from 1 to 50

# .......................................................
# for i in range(1, 5):  # i=1 2 3 4
#     print(i)
# print("End")
# DRY
# i=1 => 1
# i=2 => 2
# i=3 => 3
# i=4 => 4
# i=5 =>
# End

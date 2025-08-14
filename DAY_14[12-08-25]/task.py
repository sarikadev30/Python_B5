# Sum of Squares of all the even numbers upto 50

# 2^2+4^2+6^2+.......+50^2

# All the even numbers
# Square of a number
# Sum

# ............................................................
# n
# n=12
# for i in range(n+1):
# ..............................................................
# AP
# Arithmetic Progression Series
# 1 , 2, 3,4 ,5,6,7
# 1+1=2 => a=1 d=1
# 2+1=3
# 3+1=4
# 2 4 6 8 10
# a=2 d=2
# 2+2=4
# 1 3 5 7 9 11 13
# a=1 d=2
# 3rd term => 2nd term +d => 1st term + d + d => a+2*d
# 4th term => 3rd term +d => 2nd term +d +d => 1st term + d + d +d =>a+3*d
# 5th term => 4th term+d => 3rd term +d +d => 2nd term +d +d+d => 1st term + d+d+d+d =>a+4*d
# nth term => a+(n-1)*d

# a = 12
# d = 4
# n = 5
# for i in range(1, n + 1):
#     print(a + (i - 1) * d, end=" ")

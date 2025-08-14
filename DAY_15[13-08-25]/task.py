# GP
# GEOMETRIC PROGRESSION SERIES
#  1 2 4 8 16 32 64 128.......
# 2nd term/1st term = r (common ratio)

# 2/1=2
# 4/2=2
# 8/4=2
# 2nd term => first term * r =>  1*2 = 2
# 3rd term => 2nd term *r => first term * r *r => first term * r^2
# 4th term => 3nd term *r => 2nd term * r *r => first term * r*r*r => first term * r^3

# nth term => first term * r^(n-1)
# a , r,n  => a*r**(n-1)
# ............................................................................................
# NESTED LOOPS
#  Loops inside Loop
#  for loop
#  while loop

# for family in range(1, 6):  # 1 2 3 4 5
#     for candy in range(1, 4):  # 1 2 3
#         print(f"family-{family} ate candy-{candy}")

# for i in range(2):  # 0 1
#     for j in range(3):  # 0 1 2
#         print("Hello", i, j)
# print("End")
# i=0 => j=0   Hello 0 0
# i=0 => j=1   Hello 0 1
# i=0 => j=2   Hello 0 2

# i=1 => j=0   Hello 1 0
# i=1 => j=1   Hello 1 1
# i=1 => j=2   Hello 1 2

# i=2
# ..............................................................................................
# Father gave the son a target, of completing 10 sets. Each set contains 10 Rounds of a field.
# set 1 round 1
# set 2 round 2.....

# ..............................................................................
#  Pattern Printing

"""
**********
**********
**********
**********
**********
"""
# rows = 5
# cols = 10
# for i in range(rows):  # 0 1 2 3 4
#     for j in range(cols):  # 0 1 2 3 4 5 6 7 8 9
#         print("*", end="")
#     print()

"""
0123456789
0123456789
0123456789
0123456789
0123456789
"""
rows = 5
cols = 10
for i in range(rows):  # 0 1 2 3 4
    for j in range(cols):  # 0 1 2 3 4 5 6 7 8 9
        print(j, end="")
    print()

"""
12345678910
12345678910
12345678910
12345678910
12345678910
"""

"""
0000000000
1111111111
2222222222
3333333333
4444444444
"""

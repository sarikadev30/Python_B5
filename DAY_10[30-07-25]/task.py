# Add 5 to each element and print number from 1 to 20
# 1 => 1+5=6
# 2 => 2+5=7
# 3 => 3+5=8
# 4 => 4+5=9
# 5 => 5+5=10

# .................................................................
# Calculate sum of numbers from 1  to 10

# 1+2+3+4+5+6+7+8+9+10
# 1+2+3+4+5 => 15

i = 1
sum = 0
while i <= 10:
    sum += i
    i += 1

print("sum : ", sum)

# i=1  sum=0 1<=5 => T sum=0+1=1  i=1+1=2
# i=2 sum=1  2<=5 => T sum=1+2=3   i=2+1=3
# i=3 sum=3  3<=5 => T sum=3+3=6   i=3+1=4
# i=4 sum=6  4<=5 => T sum=6+4=10  i=4+1=5
# i=5 sum=10 5<=5 => T sum=10+5=15 i=5+1=6
# i=6 sum=15 6<=5 => F =>
# sum : 15
# .....................................................
# Calculate product of numbers from 1  to 10
# i = 1
# p = 1
# # 1*2*3*4*5
# while i <= 3:
#     p *= i
#     i += 1

# print("product : ", p)
# 1*1*1*1*1=>1
# i=1 p=1  T p=1*1=1  i=2
# i=2 p=1  T p=1*2=2  i=3
# i=3 p=2  T p=2*3=6  i=4

# .............................................................
# Print the sum of all the multiples of 3 from 0 to 40

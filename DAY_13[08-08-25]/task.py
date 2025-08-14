# Sum of these numbers
# 1+2+3+4+5=15
sum = 0
for i in range(1, 6):  # i=1 2 3 4 5
    sum += i
print(sum)

# DRY RUN
# sum=0
# i=1 sum=0+1=1 i=2
# i=2 sum=1+2=3 i=3
# i=3 sum=3+3=6 i=4
# i=4 sum=6+4=10 i=5
# i=5 sum=10+5=15 i=6
# 15
# ...............................................
# Product of these numbers
# 1*2*3*4*5 => 120
# ..........................................................
# For loop with Break

# for guest in range(1, 11):
#     if guest == 4:
#         break
#     print("Guest", guest)

# For loop with Continue

# for guest in range(1, 11):
#     print("Guest", guest)

#     if guest == 4:
#         continue

# Assignment Discussion
# Problem-6
# def isEven():
#     for i in range(1, 21):
#         if i % 2 == 0:
#             print(i)


# isEven()

# Problem-9
# Factorial of  a number
# 3! => 3*2*1 = 6


# def fact(n):
#     f = 1
#     for i in range(1, n + 1):
#         f *= i  # f=f*i
#     return f


# print(fact(3))
# fact(3)
# f=1
# i=1   (1,4) f=1*1=1  i=2
# i=2   (1,4) f=1*2=2  i=3
# i=3   (1,4) f=2*3=6  i=4
# i=4   (1,4)
#  return f => 6


# Problem-8
# fibonacci Series
# 0 1 1 2 3 5 8 13 21 34
# a b c
#   a b c


# def fib(n):
#     a = 0
#     b = 1
#     res = []
#     for i in range(n):  # 0 1 2 3 4
#         res.append(a)  # 0
#         c = a + b
#         a = b
#         b = c
#     return res


# print(fib(3))
# fib(3)
# a=0  b=1  res=[]
# i=0  (0,2) res=[0]  c=>a+b=>0+1=>1  a=>b=>1  b=>c=>1 i=1
# i=1  (0,2) res=[0,1] c=>a+b=>1+1=>2 a=>b=>1  b=>c=>2  i=2
# i=2  (0,2) res=[0,1,1] c=>a+b=> 1+2=>3 a=>b=>2   b=>c=>3  i=3
# i=3  (0,2)
# res=[0,1,1]


# Problem-10
# n=5   => 1 => 5   (2,4)=>(2,n-1)
# 0 1
# n=5
# 2 3 4
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n - 1):
#         if n % i == 0:
#             return False
#     return True


# print(is_prime(6))


# def checkPrime():
#     for i in range(1, 51):
#         if is_prime(i):
#             print(i)


# checkPrime()

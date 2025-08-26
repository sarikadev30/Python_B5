# Problem 1 :
# l = []
# for i in range(1, 6):  # 1 2 3 4 5
#     a = int(input(f"Enter number {i} :"))
#     # print(a)
#     l.append(a)

# print(l)

# Problem 2 :
# x = [1, 2, 5, 3, 4]
# fmx = x[0]  # 1  => 2
# smx = x[0]  # 1
# for i in range(len(x)):
#     if x[i] > fmx:
#         smx = fmx
#         fmx = x[i]
#     elif x[i] < fmx and x[i] > smx:
#         smx = x[i]
# print(smx, fmx)

# fmx=1
# smx=1
# i=0   => c1: x[0]>fmx => 1>1 => FALSE
#          c2: (x[0]<fmx) 1<1 FALSE  (x[0]>smx) 1>1 FALSE  F and F => F
# i=1  => c1: x[1]>fmx => 2>1 => TRUE       smx=fmx=>1       fmx=x[1]=>2
# smx=1
# fmx=2
# i=2 => c1: x[2]>fmx => 5>2 => TRUE     smx=fmx=> 2   fmx=x[2]=5
# smx=2
# fmx=5
# i=3  => c1: x[3]>fmx => 3>5 => FALSE
#         c2: (x[3]<fmx) 3<5 => TRUE  (x[3]>smx) 3>2 => TRUE  T and T => T      => smx=x[3]=3
# smx=3
# fmx=5
# i=4 => c1: x[4]>fmx => 4>5 => FALSE
#         c2: (x[4]<fmx) 4<5 => TRUE  (x[4]>smx) 4>3 => TRUE  T and T => T      => smx=x[4]=4
# smx=4
# fmx=5

n,a,b=map(int,input().split())

x="."*b
y="#"*b
ca=True
sx=[]
sy=[]
for i in range(n):
    if ca:
        sx.append(x)
        sy.append(y)
    else:
        sx.append(y)
        sy.append(x)
    ca=not ca
c=True
for i in range(n):
    for j in range(a):
        if c:
            print("".join(sx))
        else:
            print("".join(sy))
    c=not c


# c=True
# for k in range(n):
#     s=[]
#     for i in range(n):
#         if c:
#             s.append(x)
#         else:
#             s.append(y)
#         c=not c
#     for i in range(a):
#         print("".join(s))
#     c=not c
a=[int(input()) for i in range(4)]
c=0
for i in range(a[0]+1):
    if i*500>a[3]:break
    for j in range(a[1]+1):
        tmp=a[3]-(i*500+j*100)
        if tmp<0:break
        if tmp/50<=a[2]:
            c+=1
print(c)
n=int(input())
a=list(map(int,input().split()))
list.sort(a,reverse=True)
x,y=0,0
for i in range(len(a)):
    if i%2==0:
        x+=a[i]
    else:
        y+=a[i]
print(x-y)
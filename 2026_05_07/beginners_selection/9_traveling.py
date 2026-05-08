n=int(input())
txy=[list(map(int,input().split())) for _ in range(n)]
t,x,y=map(list,zip(*txy))
t.insert(0,0)
x.insert(0,0)
y.insert(0,0)
for i in range(1,len(t)):
    if abs(x[i]-x[i-1])+abs(y[i]-y[i-1])>(t[i]-t[i-1]):
        print("No")
        exit()
    if not (t[i]-t[i-1])%2==(abs(x[i]-x[i-1])+abs(y[i]-y[i-1]))%2:
        print("No")
        exit()
print("Yes")
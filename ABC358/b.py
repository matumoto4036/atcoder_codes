n,a=map(int,input().split())
t=list(map(int,input().split()))
time=0
for i in range(n):
    time=max(t[i],time)+a
    print(time)
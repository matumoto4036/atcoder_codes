x,y,n=map(int,input().split())
p=0
if 3*x>y:
    p=n//3*y+(n%3)*x
else:
    p=n*x
print(p)
w,b=map(int,input().split())
S="wbwbwwbwbwbw"
c=0
tmp=min(w//7,b//5)
w=w-tmp*7
b=b-tmp*5
for i in range(12):
    c=0
    for j in range(w+b):
        if S[(i+j)%12]=="w":
            c+=1
    if c==w:
        print("Yes")
        exit()
print("No")
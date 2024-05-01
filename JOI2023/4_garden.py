def maxflower(i,j,N):
    c=1
    n=1
    while True:
        if 0<=i-c and i+c<=N-1 and 0<=j-c and j+c<=N-1:
            if a[i][j+c]==a[i][j-c] and a[i-c][j]==a[i+c][j] and a[i][j+c]==a[i-c][j]:
                n+=1
            else:
                break
        else:
            break
        c+=1
    return n

def num_flower(n):
    tmp=1
    for i in range(2,n+1):
        tmp+=(i-1)*4
    return tmp

N=int(input())
a = [input() for i in range(N)] 
max=1
i_tmp,j_tmp=0,0
for i in range(1,N-2):
    for j in range(1,N-2):
        tmp=maxflower(i,j,N)
        if tmp>max:
            max=tmp
            i_tmp,j_tmp=i,j

print(num_flower(max))
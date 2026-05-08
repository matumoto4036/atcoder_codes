'''
6 1     
112022  
NM日にち シャツ枚数
S文字列
'''
def do(a,r,m):
    if a=="0":
        m=1
        r=0
    elif a=="1":
        if m>0:
            m-=1
        else:
            r+=1
    elif a=="2":
        r+=1
    return r,m

n,muji=map(int,input().split())
s=input()
rogo,rogomax=0,0
for i in s:
    rogo,muji=do(i,rogo,muji)
    rogomax=max(rogomax,rogo)
print(rogomax)
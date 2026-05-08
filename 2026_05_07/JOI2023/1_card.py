N=int(input())
a=list(map(int,input().split()))
a.sort()
for i in range(N-2):
  if (a[i]+3 in a):
    if (a[i]+6 in a):
      print("Yes")
      break
  if i==N-3:
    print("No")
    break
'''
3
2 5 8
'''

'''
N = int(input())
A = list(map(int, input().split()))

exist = [False] * 200020
for a in A:
    exist[a] = True
for i in range(1, 200001):
    if exist[i] and exist[i + 3] and exist[i + 6]:
        print("Yes")
        exit()
print("No")
'''
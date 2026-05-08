N=int(input())
s=input()
a,b,c=map(int,input().split())

if ("RGB" in s):
    print()

'''
rgb = 'RGB'

n = int(input())
s = str(input())
a, b, c = map(int, input().split())

ans = min(a, b) * n#全消し

opt = [a, 2 * a, 0]

for i in range(2, n):
    for j in range(0, 3):#左端3つセットで考える セットごとに3つの更新方法
        if s[i + j - 2] != rgb[j]:
            opt[i % 3] += c
    opt[i % 3] = min(opt[i % 3], (i + 1) * a)
    ans = min(ans, opt[i % 3] + (n - i - 1) * b)

print(ans)
'''

'''
GGG 
RRGB 
列ごとにループi
i-2からiまでのセットをRGBにするにはどれだけかかるか
それとそのセット全消しのどっちが安いか
'''
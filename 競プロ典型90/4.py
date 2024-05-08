# h,w=map(int,input().split())
# a=[list(map(int,input().split())) for _ in range(h)]
# at=map(list,zip(*a))
# aw=[0]*w
# ah=[0]*h
# for i in range(h):
#     for j in range(w):
#         aw[j]+=a[i][j]
#         ah[i]+=a[i][j]
# for i in range(h):
#     for j in range(w):
#         print(aw[j]+ah[i]-a[i][j],end=" ")
#     print("")


# 入力
H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

# 前処理
yoko = list(map(sum, A))
tate = list(map(sum, zip(*A)))

# 各マス
for i in range(H):
    print(' '.join(map(lambda j: str(yoko[i] + tate[j] - A[i][j]), range(W))))
#(lambda j: j**2,range(5)) 無名関数 0-4→0,1,4,9,16

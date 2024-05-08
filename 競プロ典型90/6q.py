# n,k=map(int,input().split())
# s=input()

# bubun=[]
# pre=0
# for i in range(k):
#     tmp=[]
#     tmpj=0
#     for j in range(pre,n-k+1+i):
#         tmp.append(s[j])
#         tmp.sort()
#         if tmp[0]==s[j]:tmpj=j
#     pre=tmpj+1
#     bubun.append(tmp[0])
# print("".join(bubun))

# res[i][c] := i 文字目以降で最初に文字 c が登場する index
# 存在しないときは N
def calc_next(S):
    N = len(S)
    res = [[N] * 26 for _ in range(N + 1)]
    # 後ろから見る
    for i in range(N - 1, -1, -1):
        # i + 1 文字目以降の結果を一旦 i 文字にコピー
        for j in range(26):
            res[i][j] = res[i + 1][j]
        # i 文字目の情報を反映させる
        res[i][ord(S[i]) - ord('a')] = i
    return res

N, K = map(int, input().split())
S = input()
res = ''
nex = calc_next(S)
j = -1
for i in range(K):
    for ordc in range(26):
        k = nex[j + 1][ordc]
        # ちゃんと K 文字が作れれば OK
        if N - k >= K - i:
            res += chr(ord('a') + ordc)
            j = k
            break
print(res)
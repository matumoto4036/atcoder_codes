N = int(input())
jobs = []
for i in range(N):
    d,c,s = map(int, input().split(' '))
    jobs.append({'D':d, 'C':c, 'S':s})

jobs.sort(key=lambda j:j['D'])
D_MAX = jobs[N-1]['D']

# dp[i][j]: 添字i未満の仕事をj日間で行った場合の最大報酬
dp = [[0]*(D_MAX+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,D_MAX+1):
        if j <= jobs[i-1]['D']:
            if j < jobs[i-1]['C']:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(
                    dp[i-1][j], 
                    dp[i-1][j-jobs[i-1]['C']] + jobs[i-1]['S']
                )
        else:
            dp[i][j] = dp[i][j-1]

print(dp[N][D_MAX])
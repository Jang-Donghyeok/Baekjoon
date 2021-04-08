import sys
input = sys.stdin.readline

n = int(input())
tri = []
dp = []
for i in range(n):
    num = list(map(int, input().split()))
    tri.append(num)
    dp.append([0 for _ in range(i+1)])
dp[0] = tri[0]
if n > 1:
    dp[1][0] = dp[0][0] + tri[1][0]
    dp[1][-1] = dp[0][0] + tri[1][-1]
for i in range(2, n):
    dp[i][0] = dp[i-1][0] + tri[i][0]
    dp[i][-1] = dp[i-1][1] + tri[i][-1]
    for j in range(1, i):
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + tri[i][j]

print(max(dp[n-1]))
n = int(input())
dp = [[1]*2]*n
for i in range(n):
    for j in range(2):
        dp[i][j] =
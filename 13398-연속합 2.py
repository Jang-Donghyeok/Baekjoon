import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
dp = [[0, 0] for i in range(n)]
dp[0][0] = A[0]
m = A[0]
if n > 1:
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0]+A[i], A[i])
        dp[i][1] = max(dp[i-1][0], dp[i-1][1]+A[i])
        m = max(m, dp[i][0], dp[i][1])
    print(m)
else:
    print(dp[0][0])
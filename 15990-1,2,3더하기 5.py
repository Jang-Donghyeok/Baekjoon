import sys
input = sys.stdin.readline

n = int(input())
dp= [[0]*4 for i in range(100001)]
dp[1] = [0, 1, 0, 0]
dp[2] = [0, 0, 1, 0]
dp[3] = [0, 1, 1, 1]

for i in range(n):
    num = int(input())
    for j in range(4,num+1):
        dp[j][1] = (dp[j-1][2]+dp[j-1][3]) % 1000000009
        dp[j][2] = (dp[j-2][1]+dp[j-2][3]) % 1000000009
        dp[j][3] = (dp[j-3][1]+dp[j-3][2]) % 1000000009
    print(sum(dp[num]) % 1000000009)
import sys
input = sys.stdin.readline

n = int(input())
dp= [0 for i in range(100001)]
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4,100001):
       dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for i in range(n):
    num = int(input())
    print(dp[num] % 1000000009)
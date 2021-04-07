import sys
input = sys.stdin.readline

n = int(input())
dp=[]
for i in range(n):
    num = int(input())
    dp.append(num)
dp[1] = dp[0]+dp[1]
dp[2] = max(dp[1], dp[0]+dp[2])
for i in range(3,n):
    if max(dp[i-2],dp[i-3]+dp[i-1]) == dp[i-2]:
        dp[i] = dp[i-2] +dp[i]
    else:
        dp[i] = dp[i-3] +dp[i-1]
    print(dp)
print(max(dp))
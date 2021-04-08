import sys
input = sys.stdin.readline

n = int(input())
result=[]
dp = [0]*10001
for i in range(n):
    num = int(input())
    result.append(num)
dp[1] = result[0]
if n > 1:
    dp[2] = result[0]+result[1]
for i in range(3,n+1):
    dp[i] = dp[i-3]+ result[i-2]+result[i-1]
    dp[i] = max(dp[i], dp[i-2]+result[i-1])
    dp[i] = max(dp[i], dp[i-1])
print(dp[n])
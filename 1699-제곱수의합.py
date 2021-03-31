import math

n = int(input())
dp = [1] * (n+1)
sqrt = [i*i for i in range(1,317)]
for i in range(1,n+1):
    if int(math.sqrt(i)) in sqrt:
        dp[i] =1
    else:
        dp[i] = dp[i-1] + 1
print(dp)
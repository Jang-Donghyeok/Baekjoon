import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
dp = [0]*n
for i in range(len(A)):
    for j in range(i):
        if A[j] > A[i] and dp[j] > dp[i]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))
import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
dp = [0]*n
dp2 = [0]*n
for i in range(len(A)):
    for j in range(i):
        if A[j] < A[i] and dp[j] > dp[i]:
            dp[i] = dp[j]
    dp[i] += 1
for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if A[j] < A[i] and dp2[j] > dp2[i]:
            dp2[i] = dp2[j]
    dp2[i] += 1
max = 0
for i in range(n):
    if dp[i]+dp2[i] > max:
        max = dp[i]+dp2[i]
print(max-1)
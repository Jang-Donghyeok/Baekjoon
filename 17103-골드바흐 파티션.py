import sys
input = sys.stdin.readline

n = int(input())
nums = [int(input()) for _ in range(n)]
m = max(nums)
sosu = [False,False] + [True] * (m-1)
for i in range(2, int(m**0.5)+1):
    if sosu[i]:
        for j in range(i+i, m+1, i):
            if sosu[j]:
                sosu[j] = False
for num in nums:
    count = 0
    for i in range((num//2) +1):
        if sosu[i] and sosu[num-i]:
            count += 1
    print(count)

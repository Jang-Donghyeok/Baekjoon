import sys
input = sys.stdin.readline

N, M = map(int, input().split())
num = list(map(int, input().split()))
add = 0
for i in range(0,N-2):
    for j in range(i+1, N-1):
        for k in range(j+2, N):
            if num[i] + num[j] + num[k] > M:
                continue
            else:
                add = max(add, num[i] + num[j] + num[k])
print(add)



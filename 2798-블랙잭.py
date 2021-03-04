import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
print(M)
num = deque()
num.append(map(int, input().split()))
add = 0
while True:
    if len(num) != 0:
        x = num.popleft()
        for i in range(len(num)):
            for j in range(len(num)):
                add = x + num[i] + num[j]
                if add >= M:
                    print(add)
                    break


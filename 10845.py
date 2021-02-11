from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
N = deque()
for i in range(n):
    str = input().split()
    if str[0] == 'push':
        N.append(str[1])
    elif str[0] == 'pop':
        if len(N) != 0:
            print(N.popleft())
        else:
            print(-1)
    elif str[0] == 'size':
        print(len(N))
    elif str[0] == 'empty':
        if len(N) == 0:
            print(1)
        else:
            print(0)
    elif str[0] == 'front':
        if len(N) != 0:
            print(N[0])
        else:
            print(-1)
    elif str[0] == 'back':
        if len(N) != 0:
            print(N[-1])
        else:
            print(-1)
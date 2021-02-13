import sys
from collections import deque
input = sys.stdin.readline

def Queue(str):
    if str[0] == 'push_front':
        N.appendleft(str[1])
    elif str[0] == 'push_back':
        N.append(str[1])
    elif str[0] == 'pop_front':
        if len(N) != 0:
            print(N.popleft())
        else:
            print(-1)
    elif str[0] == 'pop_back':
        if len(N) != 0:
            print(N.pop())
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
        if len(N) == 0:
            print(-1)
        else:
            print(N[0])
    elif str[0] == 'back':
        if len(N) == 0:
            print(-1)
        else:
            print(N[-1])

N = deque()
for i in range(int(input())):
    str = input().split()
    Queue(str)
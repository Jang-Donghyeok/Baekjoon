import sys
input = sys.stdin.readline

def stack(n):
    global N
    if n[0] == 'push':
        N.append(int(n[1]))
    if n[0] == 'pop':
        if len(N) == 0:
            print(-1)
        else:
            print(N.pop())
    if n[0] == 'size':
        print(len(N))
    if n[0] == 'empty':
        if len(N) == 0:
            print(1)
        else:
            print(0)
    if n[0] == 'top':
        if len(N) == 0:
            print(-1)
        else:
            s = N.pop()
            print(s)
            N.append(s)
n = int(input())
N = []
for i in range(n):
    str = list(input().split())
    stack(str)
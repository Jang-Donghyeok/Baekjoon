from collections import deque

def bfs():
    global count
    while q:
        x, cnt = q.popleft()
        if x == k:
            count = cnt
            break
        if x*2 <= k:
            q.append((x*2, cnt+1))
        if int(str(x)+'1') <= k:
            q.append((int(str(x)+'1'), cnt+1))

count = -1
n, k = map(int, input().split())
q = deque([(n, 1)])
bfs()
print(count)
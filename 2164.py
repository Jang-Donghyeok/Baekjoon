from collections import deque

n = int(input())
q = deque()
for i in range(0,n):
    q.append(i+1)
while len(q) > 1:
    q.popleft()
    change = q.popleft()
    q.append(change)
print(q[0])

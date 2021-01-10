import sys
from collections import deque
r = sys.stdin.readline

def bfs(M, N, box):
    dx = [0, 0, 1, -1]
    dy = [-1, 1 ,0 ,0]

    count = -1

    while ripe:
        count += 1
        for i in range(len(ripe)):
            x, y = ripe.popleft()

            for j in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if (0 <= nx <N) and (0 <= ny < M) and (box[nx][ny] == 0):
                    box[nx][ny] = box[x][y] + 1
                    ripe.append([nx,ny])

    for k in box:
        if 0 in k:
            return -1
    return count


M, N = map(int, r().split())
box, ripe = [], deque()
for i in range(N):
    row = list(map(int, r().split()))
    for j in range(M):
        if row[j] == 1:
            ripe.append([i, j])
    box.append(row)


print(bfs(M, N, box))
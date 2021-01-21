import sys
from collections import deque
input = sys.stdin.readline

def find(x, y):
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    q = deque()
    q.append((x,y))
    land[x][y] = 0
    while q:
        place = q.popleft()
        for i in range(8):
            nx = place[0] + direction[i][0]
            ny = place[1] + direction[i][1]

            if (0 <= nx < h) and (0 <= ny < w):
                if land[nx][ny] == 1:
                    land[nx][ny] = 0
                    q.append((nx,ny))


while True:
    w, h = map(int, input().split())
    land = []
    count = 0
    if w == 0 and h == 0:
        break
    for _ in range(h):
        cnt = list(map(int, input().split()))
        land.append(cnt)
    for i in range(h):
        for j in range(w):
            if land[i][j] != 0:
                count += 1
                find(i,j)
    print(count)

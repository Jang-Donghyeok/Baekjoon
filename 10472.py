import sys
from collections import deque
input = sys.stdin.readline


def change(box):
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]

    count = -1

    while ripe:
        count += 1
        for _ in range(len(ripe)):
            x, y = ripe.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if (0 <= nx < 3) and (0 <= ny < 3) and (box[nx][ny] == '*'):
                    box[nx][ny] = "."
                    ripe.append([nx,ny])
    return count


n = int(input())
for i in range(n):
    box, ripe = [], deque()
    for i in range(3):
        space = list(map(str, input().strip()))
        for j in range(3):
            if space[j] == "*":
                ripe.append([i, j])
        box.append(space)
    print(change(box))
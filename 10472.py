import sys
from collections import deque
input = sys.stdin.readline


def change(x,y):
    dx = [0, 0, 1, -1]
    dy = [-1, 1, 0, 0]

    count = -1

    while ripe:
        count += 1
        for i in range(len(ripe)):
            x, y = ripe.popleft()

            for j in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

              


n = int(input())
for i in range(n):
    box, ripe = [], deque()
    for i in range(3):
        space = list(map(str,input().split()))
        box.append(space)
    print(box)
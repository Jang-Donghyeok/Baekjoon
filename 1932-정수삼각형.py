import sys
input = sys.stdin.readline

n = int(input())
tri = []

for i in range(n):
    num = list(map(int, input().split()))
    tri.append(num)
for i in range(1, n):
    for j in range(len(tri[i])):
        if j == 0:
            tri[i][0] += tri[i-1][0]
        elif j == i:
            tri[i][-1] += tri[i-1][-1]
        else:
            tri[i][j] += max(tri[i-1][j-1], tri[i-1][j])
print(max(tri[n-1]))
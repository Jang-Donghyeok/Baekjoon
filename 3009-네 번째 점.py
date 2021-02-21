import sys
input = sys.stdin.readline
N = []
N2 = []
for i in range(3):
    x,y = map(int, input().split())
    N.append(x)
    N2.append(y)
for i in range(3):
    if N.count(N[i]) == 1:
        x = N[i]
    if N2.count(N2[i]) == 1:
        y = N2[i]
print(x,y)


n = int(input())
N = [['*']*n for i in range(n)]
k = 0
divide = n
while divide != 1:
    divide /= 3
    k += 1
for i in range(k):
    idx = [j for j in range(n) if (j // 3 ** i) % 3 == 1]
    for x in idx:
        for y in idx:
            N[x][y] = ' '
for _ in N:
    print("".join(_))
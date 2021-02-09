import math
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    dif = y-x
    if dif <= 3:
        print(dif)
    else:
        n = int(math.sqrt(dif))
        if dif == n ** 2:
            print(2 * n - 1)
        elif n ** 2 < dif <= n ** 2 + n:
            print(2 * n)
        else:
            print(2 * n + 1)
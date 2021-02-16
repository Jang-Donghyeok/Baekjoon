import sys
input = sys.stdin.readline

N = 123456*2 +1
check = [True] * N
for i in range(2, int(N ** 0.5) + 1):
    if check[i]:
        for j in range(2 * i, N, i):
            check[j] = False
def decimal(n):
    count = 0
    for i in range(n+1, 2*n+1):
        if check[i]:
            count += 1
    print(count)
while True:
    n = int(input())
    if n == 0:
        break
    decimal(n)
import sys
input = sys.stdin.readline

sosu = [1] * 1000001
sosu[1] = 0
for i in range(2, 1001):
    for j in range(i*2, 1000001, i):
        sosu[j] = 0
n = int(input())
for i in range(n):
    a = int(input())
    count = 0
    for j in range(1, a+1):
        if sosu[a-j] and sosu[j]:
            count += 1
    print(count)

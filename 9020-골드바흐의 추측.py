import sys
input = sys.stdin.readline

sosu = [0] *10001
sosu[1] = 1
for i in range(2,98):
    for j in range(i*2, 10001, i):
        sosu[j] = 1
n = int(input())
for i in range(n):
    a = int(input())
    b = a // 2
    for j in range(b, 1, -1):
        if sosu[a-j] ==0 and sosu[j] == 0:
            print(j, a-j)
            break






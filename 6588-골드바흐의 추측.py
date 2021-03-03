import sys
input = sys.stdin.readline

sosu = [0] *1000001
sosu[1] = 1
for i in range(2,1001):
    for j in range(i*2, 1000001, i):
        sosu[j] = 1
while True:
    a = int(input())
    if a == 0:
        break
    b = a // 2
    for j in range(1, b+1):
        if sosu[a-j] ==0 and sosu[j] == 0:
            print(a, '=' , j, '+',a-j)
            break

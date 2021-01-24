import sys
input = sys.stdin.readline

num1 = int(input())
num2 = int(input())
num3 = int(input())
NUM = str(num1 * num2 * num3)
N = []
check = {}
for _ in range(10):
    check[_] = 0
for i in range(len(NUM)):
    N.append(int(NUM[i]))
for j in range(len(N)):
    for k in check:
        if k == N[j]:
            check[k] += 1
for i in range(len(check)):
    print(check[i])
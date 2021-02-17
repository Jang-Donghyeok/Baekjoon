import sys
input = sys.stdin.readline

n = int(input())
N = []
num = list(map(int, input().split()))
Num = {}
for i in num:
    try:
        Num[i] += 1
    except:
        Num[i] = 1
result = [-1 for i in range(n)]
for i in range(len(num)):
    try:
        while N and Num[num[N[-1]]] < Num[num[i]]:
            result[N[-1]] = num[i]
            N.pop()
    except:
        pass
    N.append(i)
for i in range(len(result)):
    print(result[i], end=' ')
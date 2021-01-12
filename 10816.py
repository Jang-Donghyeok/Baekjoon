"""import sys

n = int(input())
num = list(map(int, sys.stdin.readline().split()))
n2 = int(input())
num2 = list(map(int, sys.stdin.readline().split()))
answer = {}
for i in range(len(num2)):
    count = 0
    for j in range(len(num)):
        if num2[i] == num[j]:
            count += 1
    answer[i] = count
for i in range(len(answer)):
    print(answer[i], end=" ")
"""

import sys

n = int(input())
num = list(map(int, sys.stdin.readline().split()))
num2 = list(map(int, sys.stdin.readline().split()))
answer = {}
for i in num:
    try:
        answer[i] += 1
    except:
        answer[i] = 1
result = []
for i in num2:
    try:
        result.append(answer[i])
    except:
        result.append(0)
for i in result:
    print(i, end = " ")
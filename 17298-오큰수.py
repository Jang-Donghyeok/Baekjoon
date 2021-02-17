import sys
input = sys.stdin.readline

n = int(input())
N = []
num = list(map(int, input().split()))
result = [-1 for i in range(n)]
for i in range(len(num)):
    try:
        while num[N[-1]] < num[i]:
            result[N.pop()] = num[i]
    except:
        pass
    N.append(i)
for i in range(len(result)):
    print(result[i] ,end=' ')
import sys
input = sys.stdin.readline
N = []
for i in range(9):
    tall = int(input())
    N.append(tall)
result = sum(N)
N.sort()
for i in range(9):
    for j in range(i+1, 9):
        if result-N[i]-N[j]==100:
            for k in range(9):
                if k == i or k == j:
                    continue
                else:
                    print(N[k])
            exit()


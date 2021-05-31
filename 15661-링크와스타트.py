import sys
from itertools import combinations

input = sys.stdin.readline

n = int(input())
S = [[0]*n]*n
cb = combinations(range(n), n//2)
Min = 100

for i in range(n):
    s = list(map(int, input().split()))
    S[i] = s
for c in cb:
    a = set(c)
    b = list(set(range(n)) - a)
    a = list(a)

    A, B = 0, 0
    for i in range(n//2-1):
        for j in range(i+1, n//2):
            A += S[a[i]][a[j]] + S[a[j]][a[i]]
            B += S[b[i]][b[j]] + S[b[j]][b[i]]
    Min = min(Min, abs(B-A))
print(Min)
import sys
from string import ascii_lowercase

input = sys.stdin.readline

alpha = list(ascii_lowercase)
N = {}
for i in range(len(alpha)):
    N[alpha[i]] = -1
S = input().strip()

for i in N:
    for j in range(len(S)):
        if N[i] == -1:
            if i == S[j]:
                N[i] = j
    print(N[i], end=" ")
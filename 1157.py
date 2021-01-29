import sys
from string import ascii_uppercase
input = sys.stdin.readline

n = str(input().strip())
n = n.upper()
alpha = list(ascii_uppercase)
N = {}
result =''
max = 0
for i in range(len(alpha)):
    N[alpha[i]] = 0
for i in N:
    for j in range(len(n)):
        if str(i) == n[j]:
            N[i] += 1
    if max <= N[i]:
        max = N[i]
for i in N:
    if max == N[i]:
        result += i
if len(result) >= 2:
    result = '?'
print(result)
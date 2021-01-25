import sys
input = sys.stdin.readline

N = []
N1 = []
rest = {}
count = 0
for i in range(1,11):
    num = int(input().strip())
    N.append(num % 42)
N1 = list(set(N))
for _ in range(42):
    rest[_] = 0
for i in range(len(N1)):
    for k in rest:
        if k == N1[i-1]:
            rest[k] += 1
            count += 1
print(count)
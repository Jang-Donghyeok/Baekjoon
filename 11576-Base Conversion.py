import sys
input = sys.stdin.readline

A, B = map(int, input().split())
n = int(input())
num = list(map(int, input().split()))
count, result = 0, 0
for i in num[::-1]:
    result += (i * (A**count))
    count += 1
after = []
while result:
    after.append(str(result % B))
    result //= B
print(' '.join(after[::-1]))

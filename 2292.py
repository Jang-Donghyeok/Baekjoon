import sys
input = sys.stdin.readline

n = int(input())
count = 1
i = 1
while n > 1:
    n = n - (6*i)
    i += 1
    count += 1
print(count)

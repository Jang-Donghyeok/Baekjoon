import sys
input = sys.stdin.readline

n, m = map(int, input().split())
num = list(map(int, input().split()))
for i in range(n):
    if num[i] < m:
        print(num[i], end=" ")

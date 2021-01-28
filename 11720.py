import sys
input =sys.stdin.readline

n = int(input())
num = list(map(int, input().strip()))
add = 0
for i in range(len(num)):
    add += num[i]
print(add)
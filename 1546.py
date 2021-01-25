import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
num.sort()
max = num[-1]
sum = 0
for i in range(len(num)):
    num[i] = num[i] / max * 100
    sum += num[i]
print(sum/ len(num))
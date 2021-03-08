import sys
input = sys.stdin.readline

def gcd(a, b):
    if b ==0:
        return a
    else:
        return gcd(b, a % b)

n = int(input())
for i in range(n):
    sum = 0
    num = list(map(int, input().split()))
    for j in range(1, num[0]+1):
        for k in range(j+1, num[0]+1):
            sum += gcd(num[j],num[k])
    print(sum)
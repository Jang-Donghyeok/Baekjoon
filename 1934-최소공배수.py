import sys
input = sys.stdin.readline

def gcd(a, b):
    if b ==0:
        return a
    else:
        return gcd(b, a % b)
def lcm(a, b):
    return a * b / gcd(a,b)
n = int(input())
for i in range(n):
    num1, num2 = map(int,input().split())
    print(int(lcm(num1, num2)))
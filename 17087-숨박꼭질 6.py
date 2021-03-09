import sys
input = sys.stdin.readline
def gcd(a, b):
    if b ==0:
        return a
    else:
        return gcd(b, a % b)

N, S = map(int, input().split())
A = list(map(int, input().split()))
for i in range(N):
    if A[i] > S:
        A[i] = A[i]-S
    else:
        A[i] = S - A[i]
num = min(A)
for i in range(N):
    num = gcd(num,A[i])
print(num)
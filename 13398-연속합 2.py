import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
B = []
for i in A:
      B.append(i)
B = [B]*10
for i in range(1,len(A)):
        A[i] = max(A[i], A[i-1]+A[i])
print(max(A))
for i in range(11):
        for j in range(i):
                del B[i][j]
                print(B)
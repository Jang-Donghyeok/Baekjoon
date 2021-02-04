import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    N = [i for i in range(1,n+1)]
    for i in range(k):
        for j in range(1, n):
            N[j] += N[j-1]
    print(N[-1])
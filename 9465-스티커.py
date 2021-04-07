import sys
input =sys.stdin.readline

T = int(input())
for i in range(T):
    N= []
    n = int(input())
    for i in range(2):
        t = list(map(int, input().split()))
        N.append(t)
    N[0][1] += N[1][0]
    N[1][1] += N[0][0]
    for i in range(2,n):
        N[0][i] = max(N[1][i-1], N[1][i-2])+N[0][i]
        N[1][i] = max(N[0][i-1], N[0][i-2])+N[1][i]
    print(max(N[0][n-1], N[1][n-1]))

n = int(input())
N = [0 for i in range(n+1)]
if n <= 1:
    print(n)
else:
    N[1] = 1
    N[2] = 3
    for i in range(3,n+1):
        N[i] = N[i-1] + N[i-2]*2
    print(N[n]%10007)
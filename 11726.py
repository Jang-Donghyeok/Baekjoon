n = int(input())
N = [0 for i in range(n+1)]

if n <= 3:
    print(n)
else:
    for i in range(3,n+1):
        N[1] = 1
        N[2] = 2
        N[i] = N[i-1] + N[i-2]
    print(N[i]%10007)

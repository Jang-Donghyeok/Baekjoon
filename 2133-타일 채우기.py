n = int(input())
N = [0 for i in range(n+1)]
N[1] = 0
if n > 1:
    N[2] = 3
if n % 2 == 0:
    for i in range(4, n+1, 2):
        N[i] = N[i-2] * 3
        for j in range(4,i,2):
            N[i] += N[i-j] *2
        N[i] += 2
print(N[n])

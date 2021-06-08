N, M, k = map(int, input().split())
A = [ for i in range(M)]*N]
print(A)
k = 0
for i in range(N):
    for j in range(M):
        A[i][j] = k
        k += 1
print(A)
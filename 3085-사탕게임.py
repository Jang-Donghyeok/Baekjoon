import sys
input = sys.stdin.readline

def check(N, s_row, e_row, s_col, e_col):
    n = len(N)
    result = 1
    for i in range(s_row, e_row+1):
        cnt = 1
        for j in range(1, n):
            if N[i][j-1] == N[i][j]:
                cnt += 1
            else:
                cnt = 1
            if cnt > result:
                result = cnt
    for i in range(s_col, e_col+1):
        cnt = 1
        for j in range(1,n):
            if N[j-1][i] == N[j][i]:
                cnt += 1
            else:
                cnt = 1
            if cnt > result:
                result = cnt
    return result

n = int(input())
N = [list(input()) for _ in range(n)]
result = 0

for i in range(n):
    for j in range(n):
        if j < n-1:
            N[i][j], N[i][j+1] = N[i][j+1], N[i][j]
            tmp = check(N,i,i,j,j+1)
            if tmp > result:
                result = tmp
            N[i][j], N[i][j + 1] = N[i][j + 1], N[i][j]
        if i < n-1:
            N[i][j] , N[i+1][j] = N[i+1][j] , N[i][j]
            tmp = check(N,i,i+1,j,j)
            if tmp > result:
                result = tmp
            N[i][j], N[i + 1][j] = N[i + 1][j], N[i][j]
print(result)

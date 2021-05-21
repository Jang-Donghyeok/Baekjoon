import sys
input = sys.stdin.readline

N, M = map(int, input().split())
s = []
x = []
for i in range(N):
    n = list(map(int, input().split()))
    s.append(n)
for i in range(N):
    for k in range(M):
        # 일자 - 가로
        if k + 3 < M:
            x.append(s[i][k] + s[i][k + 1] + s[i][k + 2] + s[i][k + 3])
        # 일자 - 세로
        if i + 3 < N:
            x.append(s[i][k] + s[i + 1][k] + s[i + 2][k] + s[i + 3][k])
        # 정사각형
        if k + 1 < M and i + 1 < N:
            x.append(s[i][k] + s[i][k + 1] + s[i + 1][k] + s[i + 1][k + 1])
        # ㅗ
        if k + 2 < M and i + 1 < N:
            x.append(s[i][k + 1] + s[i + 1][k] + s[i + 1][k + 1] + s[i + 1][k + 2])
        # ㅜ
        if k + 2 < M and i + 1 < N:
            x.append(s[i + 1][k + 1] + s[i][k] + s[i][k + 1] + s[i][k + 2])
        # ㅓ
        if k + 1 < M and i + 2 < N:
            x.append(s[i + 1][k] + s[i][k + 1] + s[i + 1][k + 1] + s[i + 2][k + 1])
        # ㅏ
        if k + 1 < M and i + 2 < N:
            x.append(s[i + 1][k + 1] + s[i][k] + s[i + 1][k] + s[i + 2][k])
        ##
         #
         #
        if k + 1 < M and i + 2 < N:
            x.append(s[i][k] + s[i][k + 1] + s[i + 1][k + 1] + s[i + 2][k + 1])
        ##
        #
        #
        if k + 1 < M and i + 2 < N:
            x.append(s[i][k] + s[i][k + 1] + s[i + 1][k] + s[i + 2][k])
        #
        #
        ##
        if k + 1 < M and i + 2 < N:
            x.append(s[i][k] + s[i + 1][k] + s[i + 2][k] + s[i + 2][k + 1])
         #
         #
        ##
        if k + 1 < M and i + 2 < N:
            x.append(s[i + 2][k] + s[i][k + 1] + s[i + 1][k + 1] + s[i + 2][k + 1])
        ###
        #
        if k + 2 < M and i + 1 < N:
            x.append(s[i][k] + s[i][k + 1] + s[i][k + 2] + s[i + 1][k])
          #
        ###
        if k + 2 < M and i + 1 < N:
            x.append(s[i][k + 2] + s[i + 1][k] + s[i + 1][k + 1] + s[i + 1][k + 2])
        #
        ###
        if k + 2 < M and i + 1 < N:
            x.append(s[i][k] + s[i + 1][k] + s[i + 1][k + 1] + s[i + 1][k + 2])
        ###
          #
        if k + 2 < M and i + 1 < N:
            x.append(s[i][k] + s[i][k + 1] + s[i][k + 2] + s[i + 1][k + 2])
        ###
        #
        if k + 2 < M and i + 1 < N:
            x.append(s[i][k] + s[i][k + 1] + s[i][k + 2] + s[i + 1][k])
        #
        ##
         #
        if k + 1 < M and i + 2 < N:
            x.append(s[i][k] + s[i + 1][k] + s[i + 1][k + 1] + s[i + 2][k + 1])
         #
        ##
        #
        if k + 1 < M and i + 2 < N:
            x.append(s[i][k + 1] + s[i + 1][k] + s[i + 1][k + 1] + s[i + 2][k])
        ##
         ##
        if k + 2 < M and i + 1 < N:
            x.append(s[i][k] + s[i][k + 1] + s[i + 1][k + 1] + s[i + 1][k + 2])
         ##
        ##
        if k + 2 < M and i + 1 < N:
            x.append(s[i][k + 1] + s[i][k + 2] + s[i + 1][k] + s[i + 1][k + 1])
print(max(x))
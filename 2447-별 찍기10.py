def star(n):
    global N
    global k
    while k != n+1:
        if 3 ** k == n:
            N[k][k]=''
        else:
            print(k)
            k += 1


n = int(input())
N = [['*']*n]*n
k = 0
star(n)
print(N)
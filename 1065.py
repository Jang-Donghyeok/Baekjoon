import sys
input = sys.stdin.readline

def han(n):
    N = []
    check = 100
    count = 99
    if n <= 99:
        print(n)
    else:
        while check <= n:
            N = []
            for i in list(str(check)):
                N.append(int(i))
            for j in range(-5,5):
                if N[0] == N[1] + j and N[1] == N[2] + j:
                    count += 1
            check += 1
        print(count)

n = int(input())
han(n)
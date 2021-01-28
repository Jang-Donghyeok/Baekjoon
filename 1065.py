import sys
input = sys.stdin.readline

def han(n):
    N = []
    count = 99
    if n <= 99:
        print(n)
    else:
        for i in list(str(n)):
            N.append(int(i))
        for j in range(-4,4):
            if N[0] == N[1] + j and N[1] == N[2] +j:
                count += 1
        print(count)

n = int(input())
han(n)
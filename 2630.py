import sys
input = sys.stdin.readline

white = 0
blue = 0
def cut(x,y,n):
    global white,blue
    check = N[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != N[i][j]:
                cut(x, y, n//2)
                cut(x+n//2, y, n//2)
                cut(x, y+n//2, n//2)
                cut(x+n//2, y+n//2, n//2)
                return
    if check == 0:
        white += 1
    if check == 1:
        blue += 1


n = int(input())
N = [[]*n]*n
for i in range(n):
    num = list(map(int, input().strip().split()))
    N[i] = num

cut(0, 0, n)
print(white)
print(blue)
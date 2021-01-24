import sys
input = sys.stdin.readline

N = []
N2 = []
for i in range(9):
    num = int(input())
    N.append(num)
    N2.append(num)
N.sort()
count = 0
for i in range(len(N)):
    if N[-1] == N2[i]:
        count = i+1
print(N[-1],count)
import sys
import time
start = time.time()
n = int(sys.stdin.readline())
N = []
N2 = []
for i in range(n):
    a = sys.stdin.readline().strip()
    if int(a) == 0:
        if len(N) != 0:
            N.sort()
            N2.append(int(N.pop()))
        else:
            N2.append(0)
    else:
        N.append(a)
print(N2)
print("time :", time.time() - start)  #
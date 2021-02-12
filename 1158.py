size, count = map(int, input().split())
N = []
for i in range(1,size+1):
    N.append(i)
N2 = []
loc = 0
for i in range(size):
    loc += count-1
    if loc >= len(N):
        loc = loc%len(N)
    N2.append(str(N[loc]))
    N.remove(N[loc])
print("<",", ".join(N2)[:],">", sep='')
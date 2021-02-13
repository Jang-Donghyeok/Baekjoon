start = int(input())
end = int(input())
N = []
sum = 0
def decimal(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
for i in range(start,end+1):
    if decimal(i):
        N.append(i)
if len(N) == 0:
    print(-1)
else:
    for i in range(len(N)):
        sum += N[i]
    print(sum)
    print(N[0])
import sys
input = sys.stdin.readline
start, end = map(int, input().split())
def decimal(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
for i in range(start,end+1):
    if decimal(i):
        print(i)

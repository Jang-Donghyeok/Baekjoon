import sys
input = sys.stdin.readline

n = int(input())
count = 0
while n >= 0:
    if n % 5 == 0:
        count += n//5
        print(count)
        break
    count += 1
    n -= 3
    if n <= -1:
        print(-1)
        break

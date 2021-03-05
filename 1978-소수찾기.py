n = int(input())
num = list(map(int, input().split()))
count = 0
def decimal(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
for i in num:
    if decimal(i):
        count += 1
print(count)
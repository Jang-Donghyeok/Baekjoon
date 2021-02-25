def pibo(n):
    global sum
    if n == 0:
        sum = 0
    elif n == 1:
        sum = 1
    else:
        sum = pibo(n-2) + pibo(n-1)
    return sum
n = int(input())
sum = 0
print(pibo(n))


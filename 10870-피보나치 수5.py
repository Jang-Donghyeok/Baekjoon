def pibo(n):
    global sum
    if n == 0:
        sum = 0
    elif n == 1:
        sum = 1
    else:
        for i in range(2, n+1):
            sum = pibo(i-1) + pibo(i-2)
n = int(input())
sum = 0
pibo(n)
print(sum)

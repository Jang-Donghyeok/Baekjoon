n = int(input())
N = []
result = [0]*n
for i in range(n):
    num1 = int(input())
    N.append(num1)
def add(n):
    result[0] = N[0]
    if n == 1:
        return
    result[1] = N[1] + N[0]
    if n == 2:
        return
    result[2] = max(N[0]+N[2], N[1]+N[2])
    if n == 3:
        return
    for i in range(3,n):
        result[i] = N[i] + max(N[i-1]+result[i-3], result[i-2])
add(n)
print(result[n-1])
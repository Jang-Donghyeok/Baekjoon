n = int(input())
N = list(map(int, input().split()))
sum = 0
N.sort()
for i in range(n):
    for j in range(i+1):
        sum += N[j]
print(sum)
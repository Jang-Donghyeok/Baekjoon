n = int(input())
N =[]
count = 0
end = 0
for i in range(n):
    num1, num2 = map(int, input().split())
    N.append([num1,num2])
N = sorted(N, key = lambda x : (x[1], x[0]))
for i,j in N:
    if i >= end:
        count += 1
        end = j
print(count)
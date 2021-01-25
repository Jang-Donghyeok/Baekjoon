import sys
input = sys.stdin.readline

n = int(input())
N = []
N2 = []
for i in range(n):
    sum = 0
    average = 0
    count = 0
    num = list(map(int, input().split()))
    N.append(num[:1])
    N2.append(num[1:])
    for j in N2[i]:
        sum += j
        for k in N[i]:
            average = sum / k
    for j in N2[i]:
        if average < j:
            count += 1
    print(format(count / len(N2[i])*100, ".3f") + "%")

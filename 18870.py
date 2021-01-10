n = int(input())
num = list(map(int, input().split()))
num2 = list(set(num[:]))
answer = {}
num2.sort()
for i in range(len(num2)):
    answer[num2[i]] = i
for i in num:
    print(answer[i], end=" ")

import sys
input = sys.stdin.readline

num = str(input())
if int(num) < 10:
    num = '0' + num
count = 0
num1 = num[0]
num2 = num[1]
while num != sum:
    add = str(int(num1) + int(num2))
    if int(add) >= 10:
        sum = num2 + add[1]
    else:
        sum = num2 + add[0]
    num1, num2 = sum[0], sum[1]
    count += 1
    if num == sum:
        print(123)
        break
print(count)
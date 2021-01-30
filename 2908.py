import sys
input = sys.stdin.readline

num1,num2 = list(input().split())
num1 = num1[2] + num1[1] + num1[0]
num2 = num2[2] + num2[1] + num2[0]
if int(num1) >= int(num2):
    print(num1)
else:
    print(num2)

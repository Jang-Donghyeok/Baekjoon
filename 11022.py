import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    num1, num2 = map(int, input().split())
    print("Case #"+ str(i+1) + ": "+ str(num1) + " + " + str(num2) + " = " +str(num1+num2))
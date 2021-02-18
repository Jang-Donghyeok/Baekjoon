import sys
input = sys.stdin.readline()

n = int(input())
problem = input()
num = [0]*n
for i in range(n):
    num[i] = int(input())
stack =[]
for i in problem:
    if i.isupper():
        stack.append(num[ord(i)-ord('A')])
    else:
        num1 = stack.pop()
        num2 = stack.pop()
        if i =='+':
            stack.append(num1+num2)
        elif i == '-':
            stack.append(num2-num1)
        elif i == '*':
            stack.append(num1*num2)
        elif i =='/':
            stack.append(num2/num1)
print(f'{stack[0]:.2f}')


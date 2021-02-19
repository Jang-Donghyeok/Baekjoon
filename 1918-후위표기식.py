str = input()
N = []
result =''
for i in str:
    if i.isalpha():
       result += i
    else:
        if i == '(':
            N.append(i)
        elif i == '*' or i == '/':
            while N and (N[-1] == '*' or N[-1] == '/'):
                result += N.pop()
            N.append(i)
        elif i == '+' or i == '-':
            while N and N[-1] != '(':
                result += N.pop()
            N.append(i)
        elif i == ')':
            while N and N[-1] != '(':
                result += N.pop()
            N.pop()
while N:
    result += N.pop()
print(result)




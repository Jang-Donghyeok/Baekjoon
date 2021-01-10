problem = list(input())
stack = []
answer = 0

for i in range(len(problem)):
    if problem[i] == '(':
        stack.append('(')
    else:
        if problem[i-1] == '(':
            stack.pop()
            answer += len(stack)
        else:
            stack.pop()
            answer += 1
print(answer)
n = int(input())
for i in range(n):
    str = input()
    sum = 0
    N = list(str)
    for j in N:
        if j == '(':
            sum += 1
        elif j == ')':
            sum -= 1
        if sum < 0:
            print('NO')
            break
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')

import sys
input = sys.stdin.readline

"""for i in range(int(input())):
    N1 = []
    str = input().split()
    result = ''
    for j in str:
        N = []
        for k in range(len(j)):
            N.append(j[k])
        for x in range(len(N)):
            add = N.pop()
            N1.append(add)
        N1.append(' ')
    for i in range(len(N1)):
        result += N1[i]
    print(result)"""

for i in range(int(input())):
    str = input().split()
    result = ""
    for j in str:
        j = list(j)
        j.reverse()
        j = ''.join(j)
        j += " "
        result += j
    print(result)
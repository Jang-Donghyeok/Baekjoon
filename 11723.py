import sys
input = sys.stdin.readline

def act(str, num):
    global N
    if str == 'add':
       if num not in N:
        N.append(num)
    elif str == 'remove':
        if num in N:
            N.remove(num)
    elif str == 'check':
        if num in N:
            print(1)
        else:
            print(0)
    elif str =="toggle":
        if num in N:
            N.remove(num)
        else:
            N.append(num)
    elif str == 'all':
        N = [i for i in range(1,21)]
    elif str == 'empty':
        N = []

n = int(input())
N = []
for i in range(n):
    num = input().strip()
    if num == "all" or num == "empty":
        act(num, 0)
    else:
        num = num.split()
        act(num[0], int(num[1]))

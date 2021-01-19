import sys
input = sys.stdin.readline

n = int(input())
tree = [[] for i in range(n+1)]
for i in range(n-1):
    num1, num2 = list(map(int,input().split()))
    tree[num1].append(num2)
    tree[num2].append(num1)
q=[1]
answer ={}
check = [False for i in range(n+1)]

while len(q) > 0:
    parent = q.pop(0)
    for i in tree[parent]:
        if not check[i]:
            answer[i] = parent
            q.append(i)
            check[i] = True
for i in range(n+1):
    print(answer[i])

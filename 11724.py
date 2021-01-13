import sys
input = sys.stdin.readline

def dfs(n):
    visit[n] = True
    for i in N[n]:
        print(N)
        if not visit[i]:
            dfs(i)

dot, edge = map(int, input().split())
N = [[] for i in range(dot+1)]
visit =[False] * (dot+1)
count = 0
for i in range(edge):
    line1, line2 = map(int, input().split())
    N[line1].append(line2)
    N[line2].append(line1)
for i in range(1, dot+1):
    if not visit[i]:
        count += 1
        dfs(i)
print(count)
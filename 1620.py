import sys
input = sys.stdin.readline

n, quiz = map(int,input().split())
N = []
dic = {}
for i in range(1,n+1):
    pokemon = input().strip()
    N.append(pokemon)
    dic[pokemon] = i
for i in range(quiz):
    n = input().strip()
    if n.isdigit():
        print(N[int(n)-1])
    elif n.isalpha():
        print(dic[n])
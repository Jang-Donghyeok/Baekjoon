import sys
input = sys.stdin.readline

num1, num2 = map(int, input().split())
N1 = []
N2 = []
for i in range(num1):
    name = input().strip()
    N1.append(name)
for i in range(num2):
    name = input().strip()
    N2.append(name)
dic = sorted(list(set(N1)&set(N2)))
print(len(dic))
for i in range(len(dic)):
    print(dic[i])

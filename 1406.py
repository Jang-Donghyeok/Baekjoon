import sys
input = sys.stdin.readline
N1 = list(input().strip())
N2 = []
n = int(input())
def edit(str):
    global cursor
    if str[0] == 'L' and N1 != []:
        N2.append(N1.pop())
    elif str[0] == 'D' and N2 != []:
        N1.append(N2.pop())
    elif str[0] == 'B' and N1 != []:
        N1.pop()
    elif str[0] == 'P':
        N1.append(str[1])

for i in range(n):
    str = list(input().split())
    edit(str)
print("".join(N1 + list(reversed(N2))))
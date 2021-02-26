str = input()
i = 0
N = []
while i != len(str):
    N.append(str[i:])
    i += 1
N.sort()
for i in N:
    print(i)
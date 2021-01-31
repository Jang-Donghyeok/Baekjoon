import sys
input = sys.stdin.readline

n = int(input())
count = 0
for i in range(n):
    str = input().strip()
    for j in range(len(str)):
        if j != len(str)-1:
            if str[j] == str[j+1]:
                pass
            elif str[j] in str[j+1:]:
                break
        else:
            count += 1
print(count)
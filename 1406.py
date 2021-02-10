import sys
input = sys.stdin.readline
str = input()
result = []
for i in str:
    result.append(i)
n = int(input())
N = []
cursor = len(result)
def edit(str):
    global cursor
    if str[0] == 'L':
        if cursor != 0:
            cursor -= 1
    elif str[0] == 'D':
        if cursor != (len(result)):
            cursor += 1
    elif str[0] == 'B':
        if cursor != 0:
            del result[cursor-1]
            cursor -= 1
    elif str[0] == 'P':
        result.insert(cursor, str[1])
        cursor += 1

for i in range(n):
    str = list(input().split())
    edit(str)
print("".join(result))
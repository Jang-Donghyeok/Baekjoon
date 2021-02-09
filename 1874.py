n = int(input())
N = []
result = []
count = 1
for i in range(n):
    num = int(input())
    while num >= count:
        N.append(count)
        result.append('+')
        count += 1
    if N[-1] == num:
        N.pop()
        result.append('-')
if len(N) > 0:
    print('NO')
else:
    for i in result:
        print(i)
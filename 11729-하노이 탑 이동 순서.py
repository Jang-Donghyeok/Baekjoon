n = int(input())
count = 0
move = []
def hanoi(n, start, visit, to):
    global count
    count += 1
    if n == 1:
        move.append((start,visit))
    else:
        hanoi(n-1, start, to, visit)
        move.append((start, visit))
        hanoi(n-1, to, visit,start)
hanoi(n, 1,3,2)
print(count)
for i in range(count):
    print(*move[i])
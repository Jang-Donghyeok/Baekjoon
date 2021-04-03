sum = 0
for i in range(3, -4, -1):
    print(i, end=' ')
    sum += i
    if i == -3:
        print("")
print(sum)
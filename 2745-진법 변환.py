base, num = input().split()
num = int(num)
count, result = 0, 0
for i in base[::-1]:
    if i.isdigit():
        target =int(i)
    else:
        target = ord(i) - 55
    result += (target * (num**count))
    count += 1
print(str(result))


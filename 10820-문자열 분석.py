import sys
input = sys.stdin.readline

while True:
    Acount = 0
    acount = 0
    count = 0
    space = 0
    str = input().strip('\n')
    if not str:
        break
    for i in str:
        if i.isupper():
            Acount += 1
        if i.islower():
            acount += 1
        if i.isdigit():
            count += 1
        if i.isspace():
            space += 1


    print(acount, Acount, count, space)


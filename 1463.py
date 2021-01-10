n = int(input())
count = 0
list =[n]

while list:
    if 1 in list:
       print(count)
       break
    N= []
    for i in list:
        if i % 3 == 0:
            N.append(i/3)
        if i % 2 == 0:
            N.append(i/2)
        N.append(i-1)
    list = N
    count += 1

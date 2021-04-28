import random
list = []
list2 = []
count = 0
for i in range(5):
    num = random.randint(0,9)
    if num not in list:
        list.append(random.randint(0, 9))
while len(list2) != 5:
    n = int(input("복권 번호를 입력하세요:"))
    if n not in list2:
        list2.append(n)
    else:
        print("중복된 수입니다.")
for i in list:
    for j in list2:
        if i == j:
            count += 1
if count >= 5:
    print("백만원입니다.")
elif count >= 4:
    print("50만원입니다.")
elif count >= 3:
    print("30만원입니다.")
elif count >= 2:
    print("5만원입니다.")


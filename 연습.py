import random

lucky = random.randint(10000,99999)
n = input("5자리 복권번호를 입력하시오: ")
count = 0
lucky = str(lucky)
print("당첨번호는", lucky, "입니다.")

for i in range(5):
    if lucky[i] == n[i]:
        count += 1

if count == 5:
    print("상금은 100만원입니다.")
elif count == 4:
    print("상금은 50만원입니다.")
elif count == 3:
    print("상금은 30만원입니다.")
elif count ==2:
    print("상금은 5만원입니다.")
else:
    print("꽝입니다.")
while True:
    a = int(input("a : "))
    b = int(input("b : "))
    temp = a+b-b*b
    if temp >= 0:
        print(temp)
    else:
        print("음수")
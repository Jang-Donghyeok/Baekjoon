def vsum(*num):
    sum = 0
    for i in num:
        sum += i
    return sum
print("2+3=", vsum(2, 3))
print("2+3+4=", vsum(2, 3, 4))
print("2+3+4+5=", vsum(2, 3, 4, 5))

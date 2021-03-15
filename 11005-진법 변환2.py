from string import ascii_uppercase
base = '0123456789'+ ascii_uppercase
num1, num2 = map(int, input().split())
result = ''
while num1 != 0:
    result += str(base[num1 % num2])
    num1 //= num2

print(str(result[::-1]))
str =input()
result= ''
for i in str:
    if i.isupper():
        x = ord(i) + 13
        if x > 90:
            x -= 26
        result += chr(x)
    elif i.islower():
        x = ord(i) + 13
        if x > 122:
            x -= 26
        result += chr(x)
    else:
        result += i
print(result)
str =input()
result =''
word = ''
flag = False
for i in str:
    if i == '<':
        flag = True
        word += result[::-1] + '<'
        result = ''
    elif i == '>':
        flag = False
        word += '>'
    elif i == ' ':
        if flag:
            word += ' '
        else:
            word += result[::-1] + ' '
            result = ''
    else:
        if flag:
            word += i
        else:
            result += i
word += result[::-1]
print(word)
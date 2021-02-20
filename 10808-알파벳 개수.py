"""from string import ascii_lowercase

str = input()
alpha = list(ascii_lowercase)
result =[0]*26
for i in str:
    result[alpha.index(i)] = str.count(i)
print(*result)
"""

str = input()
result = [0]*26
for i in str:
    result[ord(i)-ord('a')] += 1
print(*result)
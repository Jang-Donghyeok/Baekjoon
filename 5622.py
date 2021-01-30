import sys
from string import ascii_uppercase
input = sys.stdin.readline

alpha = str(ascii_uppercase)
count = 0
str = str(input().strip())
for i in range(len(str)):
    if str[i] in alpha[:3]:
        count += 2
    elif str[i] in alpha[3:6]:
        count += 3
    elif str[i] in alpha[6:9]:
        count += 4
    elif str[i] in alpha[9:12]:
        count += 5
    elif str[i] in alpha[12:15]:
        count += 6
    elif str[i] in alpha[15:19]:
        count += 7
    elif str[i] in alpha[19:22]:
        count += 8
    elif str[i] in alpha[22:26]:
        count += 9
count += len(str)
print(count)
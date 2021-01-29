import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    num, str = input().split()
    text =''
    for j in str:
        text += j*int(num)
    print(text)
import sys
input = sys.stdin.readline

str = input().strip()
kroati = ['c=', 'c-', 'dz=','d-', 'lj', 'nj', 's=', 'z=']

for i in kroati:
    str = str.replace(i," ")
print(len(str))